#!/usr/bin/env python

"""
Write XML file.
"""

import os
import shlex

from lxml import etree as ET
from subprocess import call, PIPE

import config as c


def write_xml_output(images):
    """Produce an XML output.
    
    This XML must be set as background under Gnome.
    See the README file for more info.
    """
    root = ET.Element('background')
    starttime = ET.SubElement(root, 'starttime')
    hour = ET.SubElement(starttime, 'hour')
    hour.text = '00'
    minute = ET.SubElement(starttime, 'minute')
    minute.text = '00'
    second = ET.SubElement(starttime, 'second')
    second.text = '01'
    size = len(images)  # save size
    images.append(images[0])    # add first element after the last
    for i in range(0, size):
        static = ET.SubElement(root, 'static')
        dur = ET.SubElement(static, 'duration')
        dur.text = c.DURATION
        file_tag = ET.SubElement(static, 'file')
        file_tag.text = c.PHOTO_DIR + images[i]
        #
        trans = ET.SubElement(root, 'transition')
        dur = ET.SubElement(trans, 'duration')
        dur.text = c.TRANSITION
        from_tag = ET.SubElement(trans, 'from')
        from_tag.text = c.PHOTO_DIR + images[i]
        to_tag = ET.SubElement(trans, 'to')
        to_tag.text = c.PHOTO_DIR + images[i+1]
    
    tree = ET.ElementTree(root)
    xml_output_file = os.path.join(c.PHOTO_DIR, c.get_xml_filename())
    tree.write(xml_output_file, pretty_print=True, 
               xml_declaration=True)
    print "# XML was written to {0}".format(xml_output_file)
# write_xml_output


def set_xml_wallpaper():
    """Set the XML file as wallpaper.
    
    Call the necessary Gnome commands for this."""
    xml_output_file = os.path.join(c.PHOTO_DIR, c.get_xml_filename())
    cmd = "gconftool-2 --type string --set /desktop/gnome/background/picture_filename {0}".format(xml_output_file)
    args = shlex.split(cmd)
    if call(args, stdout=PIPE) == 0:
        print "# XML file {0} was set as wallpaper.".format(xml_output_file)
