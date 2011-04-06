#!/usr/bin/env python

# background-fetch.py
# 
# see the README file

import urllib2
import re
import os
import os.path
import random
import sys
import Image

from BeautifulSoup import BeautifulSoup
from urlparse import urlparse
from lxml import etree as ET

# expand the list with reddit IDs if you want
reddits = { 0 : 'EarthPorn',  1 : 'CityPorn', 2 : 'SpacePorn', 
            3 : 'AnimalPorn', 4 : 'BotanicalPorn' }

# change these variables
photoDir = '/trash/gnome-wallpapers/'
duration = '895.0' # 15 minutes
transition = '5.0'
reddit = 0  # EarthPorn, by default
size_threshold = (800, 600)  # image size should have at least that many pixels
size_tolerane = 5.0          # percentage, accept image if smaller than threshold by this percentage
ratio_interval = (1.0, 2.0)  # ratio must be in this interval

# don't change these
xmlFilename = "%s.xml" % reddits[reddit]    # EarthPorn.xml, by default
reddit_url = "http://www.reddit.com/r/%s/" % reddits[reddit]

def get_image_list(url):
    # fetch html of EarthPorn homepage
    images = []
    soup = BeautifulSoup(urllib2.urlopen(url).read())
    for tag in soup.findAll('a', href=True):
        if tag['href'].lower().endswith('jpg'):
            if tag['href'] not in images:
                images.append(tag['href'])  # no duplicates and keeping the order
                
    return images
# get_image_list

def file_name(url):
    return os.path.split(urlparse(url)[2])[1]

def is_large_and_landscape(img):
    minimum_pixels = size_threshold[0] * size_threshold[1] * ((100.0 - size_tolerane)/100.0)
    im = Image.open(photoDir + file_name(img))
    large = (im.size[0] * im.size[1]) >= minimum_pixels
    ratio = float(im.size[0]) / float(im.size[1])
    landscape = im.size[0] > im.size[1]
    
    return ( large and landscape and (ratio_interval[0] <= ratio <= ratio_interval[1]) )
# is_large_and_landscape

def remove_small_or_portrait(all, filtered):
    to_remove = list( set(all).difference(set(filtered)) )
    for f in to_remove:
        file = file_name(f)
        os.remove(photoDir + file)
        
    print "# removed images: %s" % len(to_remove)
# remove_small_or_portrait

def download_images(images):
    # Use wget to download images into specified directory
    count = 0
    for image in images:
        filename = os.path.basename(image)
        if os.path.exists(photoDir + filename) is False:
            # download if the file doesn't exist yet
            os.system('wget -O ' + photoDir + filename + ' ' + image)
            count += 1
            
    print "# new image(s): %d" % count
# download_images

def write_xml_output(images):
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
    for i in range(0,size):
        static = ET.SubElement(root, 'static')
        dur = ET.SubElement(static, 'duration')
        dur.text = duration
        file = ET.SubElement(static, 'file')
        file.text = photoDir + images[i]
        #
        trans = ET.SubElement(root, 'transition')
        dur = ET.SubElement(trans, 'duration')
        dur.text = transition
        from_tag = ET.SubElement(trans, 'from')
        from_tag.text = photoDir + images[i]
        to_tag = ET.SubElement(trans, 'to')
        to_tag.text = photoDir + images[i+1]
    
    tree = ET.ElementTree(root)
    tree.write(photoDir + xmlFilename, pretty_print=True, xml_declaration=True)
# write_xml_output
    
def main():
    # get the URL of all images
    #images = get_image_list('http://www.reddit.com/r/EarthPorn/')
    images = get_image_list(reddit_url)
    
    # download images
    download_images(images)

    # filter large images and remove the small ones from the file system
    filtered = filter(is_large_and_landscape, images)
    remove_small_or_portrait(images, filtered)

    # work with these large images from now on
    images = filtered
    
    # Create an xml file
    if len(images) > 0:
        # Get all images in speficied directory
        dir_list = [x for x in os.listdir(photoDir) if x.lower().endswith('jpg')]
        random.shuffle(dir_list) # Randomize image order
        write_xml_output(dir_list)
# main

if __name__ == "__main__":
    main()
