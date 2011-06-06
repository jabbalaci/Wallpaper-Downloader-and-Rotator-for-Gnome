#!/usr/bin/env python

"""
Interaction with Gnome.

Current options: set the wallpaper.
"""

import os
import shlex

from subprocess import call, PIPE

import config as cfg


def set_wallpaper_xml():
    """Set the XML file as wallpaper.
    
    Call the necessary Gnome commands for this."""
    xml_output_file = os.path.join(cfg.PHOTO_DIR, cfg.XML_FILENAME)
    cmd = "gconftool-2 --type string --set /desktop/gnome/background/picture_filename {0}".format(xml_output_file)
    args = shlex.split(cmd)
    if call(args, stdout=PIPE) == 0:
        print("# XML file {0} was set as wallpaper.".format(xml_output_file))


def set_wallpaper_image(img, mode='stretched'):
    """Set the given file as wallpaper.
    
    Possible modes: wallpaper, centered, scaled, stretched."""
    cmd1 = "gconftool-2 --type=string --set /desktop/gnome/background/picture_options {mode}".format(mode=mode)
    cmd2 = "gconftool-2 --type=string --set /desktop/gnome/background/picture_filename {img}".format(img=img)
    
    call(shlex.split(cmd1), stdout=PIPE)
    call(shlex.split(cmd2), stdout=PIPE)
