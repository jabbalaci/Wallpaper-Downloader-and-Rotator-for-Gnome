#!/usr/bin/env python

"""
Resize images.
"""

import Image

import config as cfg


METHOD = Image.BILINEAR


def resize_to_screen_width(file_path):
    """Resize a large image to screen width.
    
    Image ratio is kept."""
    print "# resizing image...",
    img = Image.open(file_path)
    width, height = img.size
    
    ratio = float(width) / float(cfg.MAX_WIDTH)
    new_width = int(float(width) / ratio)
    new_height = int(float(height) / ratio)

    img = img.resize((new_width, new_height), METHOD)
    img.save(file_path)
    print "done."
