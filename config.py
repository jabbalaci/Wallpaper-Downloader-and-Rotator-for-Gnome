#!/usr/bin/env python

"""
Project configuration.
"""

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

##############################################################################
## change these variables
##############################################################################
# Your choice. Example: 0, which means EarthPorn.
CHOICE = 3
# Base dir. Set in ABSOLUTE path.
BASE_DIR = '/trash/gnome-wallpapers'
# Where to save the images. Example: /trash/gnome-wallpapers/EarthPorn
PHOTO_DIR = '{base_dir}/{dir}/'.format(base_dir=BASE_DIR, dir=WALLPAPER_PAGES[CHOICE]['id'])
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
    return WALLPAPER_PAGES[CHOICE]
