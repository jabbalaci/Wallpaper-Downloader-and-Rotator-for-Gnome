#!/usr/bin/env python

"""
background_fetch.py

Download images from /r/EarthPorn (or from other reddits) and 
create a rotating background XML for Gnome.

See the README file for more details.
"""

import os
import random
import Image

from urlparse import urlparse

import wallpapers.helper.config as c
import wallpapers.helper.database as db
from wallpapers.helper import xml
from wallpapers.scraper import reddit


def get_file_name(url):
    """Return the file name from an URL.
       
    Ex.: http://example/pic.jpg => pic.jpg.
    """
    return os.path.split(urlparse(url)[2])[1]


def is_ok_for_wallpaper(image):
    """Decide whether an image is appropriate as a wallpaper.
    
    An image is good if (1) it's resolution is large enough,
    (2) rotation is landscape, and (3) ratio is OK.
    """
    minimum_pixels = c.SIZE_THRESHOLD[0] * c.SIZE_THRESHOLD[1] * \
                     ((100.0 - c.SIZE_TOLERANCE)/100.0)
    file_name = get_file_name(image)
    try:
        img = Image.open(c.PHOTO_DIR + file_name)
    except IOError:
        print "# warning: I/O error with {0}.".format(file_name)
        return False
    # else, if the image could be opened
    width, height = img.size
    
    large = (width * height) >= minimum_pixels
    landscape = width > height
    ratio = float(width) / float(height)
    ratio_ok = (c.RATIO_INTERVAL[0] <= ratio <= c.RATIO_INTERVAL[1])
    
    return ( large and landscape and ratio_ok )
# is_ok_for_wallpaper


def register_good_and_bad_images_to_db(good_images, bad_images):
    for img in good_images:
        db.add_image(img)
        
    for img in bad_images:
        db.add_image(img, good=False)
# register_good_and_bad_images_to_db
        

def remove_bad_images(bad_images):
    """Remove images that are not so good for a wallpaper."""
    for img in bad_images:
        os.remove(c.PHOTO_DIR + get_file_name(img))
        
    print "# removed image(s): {0}".format(len(bad_images))
# remove_bad_images


def download_images(images):
    """Use wget to download new images into a specified directory."""
    fetched = []
    count = 0
    for img in images:
        if not db.is_image_in_db(img):
            filename = os.path.basename(img)
            if not os.path.exists(c.PHOTO_DIR + filename):
                cmd = "wget {0} -O {1}".format(img, os.path.join(c.PHOTO_DIR, filename))
                os.system(cmd)
                fetched.append(img)
                count += 1
        else:
            print "# {0} was already fetched once...".format(img)
            
    print "# new img(s): %d" % count
    return fetched
# download_images


def create_and_set_xml_wallpaper():
    """Collect images, create an XML and set it as wallpaper."""
    # get all images in the speficied directory
    jpg_files = [x for x in os.listdir(c.PHOTO_DIR) if x.lower().endswith('jpg')]
    if len(jpg_files) > 0 and c.PRODUCE_XML:
        random.shuffle(jpg_files) # randomize image order
        xml.write_xml_output(jpg_files)
        if c.SET_XML_WALLPAPER:
            xml.set_xml_wallpaper()


def main():
    """Control block."""
    db.init()
    
    all_images = reddit.get_image_url_list(c.get_reddit_url())
    
    fetched_images = download_images(all_images)

    good_images = [x for x in fetched_images if is_ok_for_wallpaper(x)]
    bad_images = list( set(fetched_images).difference(set(good_images)) )
    
    register_good_and_bad_images_to_db(good_images, bad_images)
    remove_bad_images(bad_images)

    create_and_set_xml_wallpaper()
# main

#############################################################################

if __name__ == "__main__":
    main()
