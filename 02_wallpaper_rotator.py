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
    print "# Jabba's Wallpaper Rotator for Gnome v0.1"
    print "# initial photo dir.: {dir}".format(dir=cfg.PHOTO_DIR)
    print "# initial duration: {0} sec.".format(cfg.DURATION)


def main():
    print_info()
    
    prev = None
    while True:
        # if you modify the config file, this script doesn't have to be restarted
        reload(cfg)
        
        images = [os.path.join(cfg.PHOTO_DIR, x) for x in os.listdir(cfg.PHOTO_DIR) if x.lower().endswith('jpg')]
        random.shuffle(images)
        nb_images = len(images)
        
        if nb_images == 0:
            # there are no images in the directory => do nothing
            pass
        
        if nb_images == 1:
            # there is only one image => easy choice
            wallpaper = images[0]
            
        if nb_images > 1:
            # there are several images => choose a different image than the previous pick
            wallpaper = random.choice(images)
            while wallpaper == prev:
                wallpaper = random.choice(images)
            gnome.set_wallpaper_image(wallpaper)
            prev = wallpaper
            
        try:
            sleep(float(cfg.DURATION))
        except KeyboardInterrupt:
            sys.exit()

#############################################################################

if __name__ == "__main__":
    main()
