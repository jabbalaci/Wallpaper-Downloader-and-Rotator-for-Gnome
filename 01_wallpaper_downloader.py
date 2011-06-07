#!/usr/bin/env python

"""
wallpapers.py

Download images from /r/EarthPorn (or from other reddits) and 
create a rotating background XML for Gnome.

See the README file for more details.
"""

import os
import random
import Image

from urlparse import urlparse

import config as cfg
import wallpapers.helper.database as db
from wallpapers.helper import xml
from wallpapers.helper import gnome
from wallpapers.scraper import dispatch
from wallpapers.helper import directories
from wallpapers.helper import resize


cnt_resized_images = 0


def get_file_name(url):
    """Return the file name from an URL.
       
    Ex.: http://example/pic.jpg => pic.jpg.
    """
    return os.path.split(urlparse(url)[2])[1]


def is_ok_for_wallpaper(image_url):
    """Decide whether an image_url is appropriate as a wallpaper.
    
    An image_url is good if (1) it's resolution is large enough,
    (2) rotation is landscape, and (3) ratio is OK.
    """
    minimum_pixels = cfg.SIZE_THRESHOLD[0] * cfg.SIZE_THRESHOLD[1] * \
                     ((100.0 - cfg.SIZE_TOLERANCE_PERCENTAGE)/100.0)
    file_name = get_file_name(image_url)
    file_path = cfg.PHOTO_DIR + file_name
    try:
        img = Image.open(file_path)
    except IOError:
        print("# warning: I/O error with {0}".format(file_name))
        return False
    # else, if the image could be opened
    width, height = img.size
    
    large = (width * height) >= minimum_pixels
    landscape = width > height
    ratio = float(width) / float(height)
    ratio_ok = (cfg.RATIO_INTERVAL[0] <= ratio <= cfg.RATIO_INTERVAL[1])
    
    ok_for_wallpaper = (large and landscape and ratio_ok)
        
    return ok_for_wallpaper


def register_good_and_bad_image_urls_to_db(good_images, bad_images):
    """Store image URLs in the DB and indicate if they are good or bad.""" 
    for img in good_images:
        db.add_image(img)
        
    for img in bad_images:
        db.add_image(img, good=False)


def delete_bad_images(bad_image_urls):
    """Delete images from the file system that are not suitable for wallpapers."""
    for url in bad_image_urls:
        os.remove(cfg.PHOTO_DIR + get_file_name(url))

    print("# removed image(s): {0}".format(len(bad_image_urls)))

    
def download_images(image_urls):
    """Use wget to download new images into a specified directory."""
    fetched = []
    count = 0
    for img_url in image_urls:
        if not db.is_image_in_db(img_url):
            filename = os.path.basename(img_url)
            if not os.path.exists(cfg.PHOTO_DIR + filename):
                cmd = "wget {0} -O {1}".format(img_url, os.path.join(cfg.PHOTO_DIR, filename))
                os.system(cmd)
                fetched.append(img_url)
                count += 1
        else:
            print("# {0} was already fetched once...".format(img_url))

    print("# new imgage(s): {0}".format(count))
    return fetched


def create_and_set_xml_wallpaper():
    """Collect images, create an XML and set it as wallpaper."""
    if cfg.PRODUCE_XML:
        jpg_files = [x for x in os.listdir(cfg.PHOTO_DIR) if x.lower().endswith('jpg')]
        if len(jpg_files) > 0:
            random.shuffle(jpg_files)   # randomize image order
            xml.write_xml_output(jpg_files)
            if cfg.SET_XML_WALLPAPER:
                gnome.set_wallpaper_xml()


def header():
    """Header to know which site we are working with."""
    header = "{0}".format(cfg.get_current_site_record()['url'])
    size = len(header) + 2 + 2
    return """{sep}
# {header} #
{sep}""".format(sep='#'*size, header=header) 


def resize_large_images(image_urls):
    """Resize wallpaper images that are too large."""
    global cnt_resized_images
    
    for image_url in image_urls:
        file_name = get_file_name(image_url)
        file_path = cfg.PHOTO_DIR + file_name
        img = Image.open(file_path)
        width = img.size[0]
        if width > cfg.MAX_WIDTH:
            resize.resize_to_screen_width(file_path)
            cnt_resized_images += 1


def get_images_from_site(site_key):
    """Get images from a given site."""
    cfg.set_current_choice(site_key)
    directories.check_photo_dir()
    
    print header()

    all_image_urls = dispatch.get_images(cfg.get_current_site_record())
    
    fetched_image_urls = download_images(all_image_urls)

    good_image_urls = [x for x in fetched_image_urls if is_ok_for_wallpaper(x)]
    bad_image_urls = list( set(fetched_image_urls).difference(set(good_image_urls)) )
    
    register_good_and_bad_image_urls_to_db(good_image_urls, bad_image_urls)
    delete_bad_images(bad_image_urls)
    
    if cfg.RESIZE_LARGE_IMAGES:
        resize_large_images(good_image_urls)

    
def main():
    """Control block."""
    cfg.self_verify()
    directories.check_base_dir()
    db.init()
    
    save_choice = cfg.CURRENT_CHOICE
    
    for site_key in cfg.MULTIPLE_CHOICE:
        get_images_from_site(site_key)
        
    cfg.set_current_choice(save_choice)
    
    create_and_set_xml_wallpaper()
    print "#"
    print "# total number of resized images: {cnt}".format(cnt=cnt_resized_images)

#############################################################################

if __name__ == "__main__":
    main()
