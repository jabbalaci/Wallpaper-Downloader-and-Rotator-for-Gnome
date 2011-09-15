#!/usr/bin/env python

"""
Controller for extracting images from various sites.
"""

import config as cfg
import reddit
import wallbase
import four_walled


def get_images(page_dict):
    result = []
    if page_dict['type'] == cfg.REDDIT_COM:
        result = reddit.get_image_url_list(page_dict['url'])
    elif page_dict['type'] == cfg.WALLBASE_CC:
        result = wallbase.get_image_url_list(page_dict['url'])
    elif page_dict['type'] == cfg.FOUR_WALLED_ORG:
        result = four_walled.get_image_url_list(page_dict['url'])
        
    return result 