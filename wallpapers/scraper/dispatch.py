#!/usr/bin/env python

"""
Controller for extracting images from various sites.
"""

import config as cfg
import reddit


def get_images(page_dict):
    result = []
    if page_dict['type'] == cfg.REDDIT_COM:
        result = reddit.get_image_url_list(page_dict['url'])
        
    return result 