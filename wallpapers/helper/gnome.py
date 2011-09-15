#!/usr/bin/env python

"""
Interaction with Gnome.

Current options: set the wallpaper.
"""

import shlex

from subprocess import call, PIPE


def set_wallpaper_image(img, mode='stretched'):
    """Set the given file as wallpaper.
    
    Possible modes: wallpaper, centered, scaled, stretched."""
    cmd1 = "gconftool-2 --type=string --set /desktop/gnome/background/picture_options {mode}".format(mode=mode)
    cmd2 = "gconftool-2 --type=string --set /desktop/gnome/background/picture_filename {img}".format(img=img)
    
    call(shlex.split(cmd1), stdout=PIPE)
    call(shlex.split(cmd2), stdout=PIPE)
