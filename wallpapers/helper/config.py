#!/usr/bin/env python

"""
constants
"""

# expand the list with REDDIT IDs if you want
REDDITS = {
    0 : 'EarthPorn',  
    1 : 'CityPorn', 
    2 : 'SpacePorn', 
    3 : 'AnimalPorn', 
    4 : 'BotanicalPorn', 
    5 : 'AlternativeArt', 
}

##############################################################################
## change these variables
##############################################################################
# where to save the images:
PHOTO_DIR = '/trash/gnome-wallpapers/'
# SQLite database will be stored here:
SQLITE_DB = '/trash/gnome-wallpapers/database/wallpapers.sqlite'
# EarthPorn, by default:
REDDIT = 0
# image size should have at least that many pixels:
SIZE_THRESHOLD = (900, 600)
# percentage, accept image if smaller than threshold by this percentage:
SIZE_TOLERANCE = 5.0
# ratio must be in this interval:
RATIO_INTERVAL = (1.0, 2.0)
##############################################################################
## for Gnome's XML
##############################################################################
# Should we produce an XML? It's not obligatory. You can use this script
# for simply downloading images and you can use a different wallpaper manager. 
#PRODUCE_XML = True
PRODUCE_XML = False
# Should we set the produced XML as your wallpaper? If PRODUCE_XML is False,
# it will be discarded.
#SET_XML_WALLPAPER = True
SET_XML_WALLPAPER = False
# 10 minutes:
DURATION = '600.0'
# transition time between two images:
TRANSITION = '3.0'
##############################################################################


def get_xml_filename():
    """XML output file's name.
    
    Default value: EarthPorn.xml.
    """
    return "{0}.xml".format(REDDITS[REDDIT]) 


def get_reddit_url():
    """URL of the reddit where we want to get the images."""
    return "http://www.reddit.com/r/{0}/".format(REDDITS[REDDIT])
