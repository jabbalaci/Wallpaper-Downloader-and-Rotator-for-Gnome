#!/usr/bin/env python

"""
My own wallpaper changer. 

I was not satisfied with the existing solutions so I made my own :)

Usage:
======
 
Simply launch it in the background. 
You can also put it among the startup applications.
"""

import os
import sys
import random

from time import sleep

import config as cfg
from wallpapers.helper import gnome


def print_info():
    li = [cfg.get_photo_dir_by_key(key) for key in cfg.ROTATOR_CHOICE]

    print "# Jabba's Wallpaper Rotator for Gnome v0.2"
    print "#", li
    print "# initial duration: {0} sec.".format(cfg.DURATION)


class WallpaperPicker:
    """Simple class for collecting images and picking one randomly."""
    
    def __init__(self):
        """To prevent picking the previous image."""
        self.prev = None
        
    def collect_images(self):
        """Collect images from _several_ directories."""
        li = []
        for key in cfg.ROTATOR_CHOICE:
            photo_dir = cfg.get_photo_dir_by_key(key)
            li.extend([os.path.join(photo_dir, x) for x in os.listdir(photo_dir) if x.lower().endswith('jpg')])
        self.images = li
        
    def get_nb_images(self):
        """Number of images."""
        return len(self.images)
    
    def get_first_image(self):
        """Get the first image."""
        return self.images[0]
    
    def get_random_image(self):
        """Get a random image from the list."""
        random.shuffle(self.images)
        img = random.choice(self.images)
        while img == self.prev:
            img = random.choice(self.images)
        self.prev = img
        
        return img


def main():
    print_info()
    
    wp = WallpaperPicker()
    
    while True:
        # if you modify the config file, this script doesn't have to be restarted
        reload(cfg)
        cfg.self_verify()
        
        wp.collect_images()
        
        nb_images = wp.get_nb_images()
        
        if nb_images == 0:
            # there are no images in the directory => do nothing
            pass
        
        if nb_images == 1:
            # there is only one image => easy choice
            wallpaper = wp.get_first_image()
            
        if nb_images > 1:
            # there are several images => choose a different image than the previous pick
            wallpaper = wp.get_random_image()
            gnome.set_wallpaper_image(wallpaper)
            
        try:
            sleep(float(cfg.DURATION))
        except KeyboardInterrupt:
            sys.exit()

#############################################################################

if __name__ == "__main__":
    main()
