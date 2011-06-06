#!/usr/bin/env python

"""
Check directories if they exist. If not, create them.
"""

import os
import sys

import config as cfg


def check_base_dir():
    if not os.path.exists(cfg.BASE_DIR):
        print >>sys.stderr, "Error: the base directory {dir} doesn't exist.".format(dir=cfg.BASE_DIR)
        sys.exit(1)
    
        
def check_photo_dir():
    if not os.path.exists(cfg.PHOTO_DIR):
        os.makedirs(cfg.PHOTO_DIR)
