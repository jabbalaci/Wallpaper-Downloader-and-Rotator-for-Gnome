#!/usr/bin/env python

"""Script to download images from /r/EarthPorn and create a rotating background

Change the following variables to the values appropriate for your computer
* photoDir
* duration
* transition
* xmlFilename

This script will download all the jpg images from the front page of /r/EarthPorn
It will then create a randomized xml file that Gnome can use to automatically transition
between desktop images at a specified interval.

To set this as your background, just select the xml file created as your desktop
background (you'll need to change the filter from "Images" to "All Files") See the
following URL for a screenshot:
http://dragonseptarts.files.wordpress.com/2010/06/screenshot-add-wallpaper1.png

I've added this file to my crontab set to run once a day.

TODO: Evaluate images for desktop suitability (ignore unsuitable resolutions or sizes)
"""

import urllib2
import re
import os
import random

def main():
    # Change these variables
    photoDir = '/home/jabba/wallpapers/earthporn/'
    duration = '855.0' # 15 minutes
    transition = '5.0'
    xmlFilename = 'EarthPorn.xml'

    # Fetch html of EarthPorn homepage
    response = urllib2.urlopen('http://www.reddit.com/r/EarthPorn/')
    html = response.read()

    # Scrape page to find all jpg links
    jpgRe = re.compile('href="([^"]*jpg)"', re.IGNORECASE)
    scrape = jpgRe.findall(html)

    # Create new list and remove duplicates
    images = []
    for image in scrape:
        if image in images:
            pass
        else:
            images.append(image)

    # Use wget to download images into specified directory
    count = 0
    for image in images:
        filename = os.path.basename(image)
        if os.path.exists(photoDir + filename):
            # Don't download if it already exists
            pass
        else:
            os.system('wget -O ' + photoDir + filename + ' ' + image)
            count = count + 1
    print "%d New Images" % count

    # Create an xml file
    if count > 0:
        # Get all images in speficied directory
        dirList = os.listdir(photoDir)
        oldfile = ''
        firstfile = ''
        first = True
        random.shuffle(dirList) # Randomize image order

        xml = '''<background>
        <starttime>
            <hour>0</hour>
            <minute>00</minute>
            <second>01</second>
        </starttime>'''
        for fname in dirList:
            if fname.endswith('jpg'):
                if first: 
                    firstfile = fname
                else:
                    xml += '''
        <transition>
            <duration>{0}</duration>
            <from>{1}</from>
            <to>{2}</to>
        </transition>'''.format(transition, photoDir + oldfile, photoDir + fname)
            xml += '''
        <static>
            <duration>{0}</duration>
            <file>{1}</file>
        </static>'''.format(duration, photoDir + fname)

            oldfile = fname
            first = False
        xml += '''
        <transition>
            <duration>{0}</duration>
            <from>{1}</from>
            <to>{2}</to>
        </transition>
    </background>'''.format(transition, photoDir + oldfile, photoDir + firstfile)

        xmlfile = open(photoDir + xmlFilename, 'w')
        xmlfile.write(xml)
        xmlfile.close()

if __name__ == "__main__":
    main()
