#!/usr/bin/env python

"""
Project configuration.
"""

import sys

# Base dir. Set it in ABSOLUTE path. No slash at the end.
# Images will be saved here.
BASE_DIR = '/trash/gnome-wallpapers'

# types of websites
REDDIT_COM = 0
WALLBASE_CC = 1     # TODO

# expand the list if you want
WALLPAPER_PAGES = {
    0 : {'id': 'EarthPorn',      'type': REDDIT_COM, 'url': 'http://www.reddit.com/r/EarthPorn'},
    1 : {'id': 'CityPorn',       'type': REDDIT_COM, 'url': 'http://www.reddit.com/r/CityPorn'},
    2 : {'id': 'SpacePorn',      'type': REDDIT_COM, 'url': 'http://www.reddit.com/r/SpacePorn'},
    3 : {'id': 'AnimalPorn',     'type': REDDIT_COM, 'url': 'http://www.reddit.com/r/AnimalPorn'},
    4 : {'id': 'BotanicalPorn',  'type': REDDIT_COM, 'url': 'http://www.reddit.com/r/BotanicalPorn'},
    5 : {'id': 'AlternativeArt', 'type': REDDIT_COM, 'url': 'http://www.reddit.com/r/AlternativeArt'},
}

# Your choice. Example: 0, which means EarthPorn.
CURRENT_CHOICE = 3
# The downloader can grab images from _several_ sites too. Precise their keys here _in a list_.
# This list should contain at least one element, the CURRENT_CHOICE.
#MULTIPLE_CHOICE = [CURRENT_CHOICE]
# variations:
#MULTIPLE_CHOICE = [0,1,2]    # EarthPorn, CityPorn, and SpacePorn
MULTIPLE_CHOICE = WALLPAPER_PAGES.keys()    # all of them

# this is for wallpaper_rotator.py
# images will be chosen from this (or these) category(s)
# it's a _list_
ROTATOR_CHOICE = WALLPAPER_PAGES.keys()    # all of them
#ROTATOR_CHOICE = [3]

def get_curr_photo_dir():
    """Get the current photo dir.
    
    It must be here to be visible."""
    return '{base_dir}/{dir}/'.format(base_dir=BASE_DIR, dir=WALLPAPER_PAGES[CURRENT_CHOICE]['id'])

def get_photo_dir_by_key(key):
    """Get the photo dir. of the given key."""
    return '{base_dir}/{dir}/'.format(base_dir=BASE_DIR, dir=WALLPAPER_PAGES[key]['id'])

##############################################################################
## change these variables if you want
##############################################################################
# Where to save the images. Example: /trash/gnome-wallpapers/EarthPorn
PHOTO_DIR = get_curr_photo_dir()
# SQLite database will be stored here:
SQLITE_DB = '{base_dir}/.database/wallpapers.sqlite'.format(base_dir=BASE_DIR)
# image size should have at least that many pixels:
SIZE_THRESHOLD = (900, 600)
# accept image if smaller than threshold by this percentage:
SIZE_TOLERANCE_PERCENTAGE = 5.0
# ratio must be in this interval:
RATIO_INTERVAL = (1.0, 2.1)
##############################################################################
## for Gnome's XML
##############################################################################
XML_FILENAME = 'wallpapers.xml'
# Should we produce an XML? It's not obligatory. You can use this script
# for simply downloading images and you can use a different wallpaper manager. 
#PRODUCE_XML = True
PRODUCE_XML = False
# Should we set the produced XML as your wallpaper? If PRODUCE_XML is False,
# it will be discarded.
#SET_XML_WALLPAPER = True
SET_XML_WALLPAPER = False
# duration in seconds:
DURATION = '600.0'
# transition time in seconds between two images:
TRANSITION = '3.0'
##############################################################################


def get_choice():
    """Get the chosen record as a dictionary."""
    return WALLPAPER_PAGES[CURRENT_CHOICE]


def set_current_choice(choice):
    """Set the current choice. Update photo dir. too."""
    global CURRENT_CHOICE, PHOTO_DIR
    
    CURRENT_CHOICE = choice
    PHOTO_DIR = get_curr_photo_dir()


def self_verify():
    """Let's do some verifications to be sure that everythign was set correctly."""
    global BASE_DIR, MULTIPLE_CHOICE, ROTATOR_CHOICE
    
    if BASE_DIR.endswith('/'):      # remove trailing slash
        BASE_DIR = BASE_DIR[:-1]
        
    if CURRENT_CHOICE not in WALLPAPER_PAGES.keys():
        print >>sys.stderr, "Error: your CURRENT_CHOICE in the config file is invalid."
        sys.exit(2)
        
    if CURRENT_CHOICE not in MULTIPLE_CHOICE:
        print >>sys.stderr, "Error: CURRENT_CHOICE must be included in MULTIPLE_CHOICE."
        sys.exit(2)
         
    MULTIPLE_CHOICE = sorted(list(set(MULTIPLE_CHOICE)))    # remove duplicates
    for e in MULTIPLE_CHOICE:
        if e not in WALLPAPER_PAGES.keys():
            print >>sys.stderr, "Error: MULTIPLE_CHOICE contains an invalid entry."
            sys.exit(2)

    if len(ROTATOR_CHOICE) == 0:
        print >>sys.stderr, "Error: ROTATOR_CHOICE cannot be empty."
        sys.exit(2)
        
    ROTATOR_CHOICE = list(set(ROTATOR_CHOICE))    # remove duplicates
    for e in ROTATOR_CHOICE:
        if e not in WALLPAPER_PAGES.keys():
            print >>sys.stderr, "Error: ROTATOR_CHOICE contains an invalid entry."
            sys.exit(2)
