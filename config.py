#!/usr/bin/env python

"""
Project configuration.

New: only JPG images are downloaded from now on (PNG support is dropped).
"""

import sys

# Base dir. Set it in ABSOLUTE path. No slash at the end.
# Images will be saved here.
BASE_DIR = '/trash/gnome-wallpapers'

# types of websites
REDDIT_COM = 0
WALLBASE_CC = 1
FOUR_WALLED_ORG = 2     # 4walled.org

# Wallbase info
# -------------
#
# See http://wallbase.cc/tags for a list of tags. If you click on 'Star Wars'
# for instance, you'll be redirected to http://wallbase.cc/tags/info/7964.
# This is what you should add to the list below. To the ID, I suggest adding
# the 'wb_' prefix to differentiate it from subreddits.

def get_4walled_url(tag, sfw):
    # at 4walled.org sfw=0 means you want sfw images
    template = 'http://4walled.org/search.php?tags={tag}&board=&width_aspect=&searchstyle=larger&sfw={sfw}&search=search'
    return template.format(tag=tag, sfw = '0' if sfw else '')

# expand the list if you want
WALLPAPER_PAGES = {
    ### add subreddits below:
    0 : {'id': 'EarthPorn',      'type': REDDIT_COM,  'url': 'http://www.reddit.com/r/EarthPorn'},
    1 : {'id': 'CityPorn',       'type': REDDIT_COM,  'url': 'http://www.reddit.com/r/CityPorn'},
    2 : {'id': 'SpacePorn',      'type': REDDIT_COM,  'url': 'http://www.reddit.com/r/SpacePorn'},
    3 : {'id': 'AnimalPorn',     'type': REDDIT_COM,  'url': 'http://www.reddit.com/r/AnimalPorn'},
    4 : {'id': 'BotanicalPorn',  'type': REDDIT_COM,  'url': 'http://www.reddit.com/r/BotanicalPorn'},
    5 : {'id': 'NaturePics',     'type': REDDIT_COM,  'url': 'http://www.reddit.com/r/NaturePics'},
    6 : {'id': 'WaterPorn',      'type': REDDIT_COM,  'url': 'http://www.reddit.com/r/WaterPorn'},
    7 : {'id': 'AlternativeArt', 'type': REDDIT_COM,  'url': 'http://www.reddit.com/r/AlternativeArt'},
    8 : {'id': 'SpecArt',        'type': REDDIT_COM,  'url': 'http://www.reddit.com/r/SpecArt'},
    ### add wallbase pages below:
    #9 : {'id': 'wb_Random',      'type': WALLBASE_CC, 'url': 'http://wallbase.cc/random'},
   10 : {'id': 'wb_StarWars',    'type': WALLBASE_CC, 'url': 'http://wallbase.cc/tags/info/7964'},
   11 : {'id': 'wb_Girls',       'type': WALLBASE_CC, 'url': 'http://wallbase.cc/tags/info/7926'},  # strictly after Star Wars ;)
   12 : {'id': 'wb_Linux',       'type': WALLBASE_CC, 'url': 'http://wallbase.cc/tags/info/8718'},
   13 : {'id': 'wb_Ubuntu',      'type': WALLBASE_CC, 'url': 'http://wallbase.cc/tags/info/8719'},
   14 : {'id': 'wb_Space',       'type': WALLBASE_CC, 'url': 'http://wallbase.cc/tags/info/8135'},
   ### add 4walled pages below:
   15 : {'id': '4w_Linux',       'type': FOUR_WALLED_ORG, 'url': get_4walled_url(tag='linux', sfw=True)},
}

# Your choice. Example: 0, which means EarthPorn.
CURRENT_CHOICE = 0
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

# Should large images be resized?
RESIZE_LARGE_IMAGES = True
#RESIZE_LARGE_IMAGES = False
# Here you can specify the width of your screen in pixels.
# Too large images will be resized to this width.
MAX_WIDTH = 1920
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


def get_current_site_record():
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
