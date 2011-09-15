#!/usr/bin/env python

"""
Working with webpages, URLs, etc.
"""

import os

from urlparse import urlparse


def get_host(url):
    """Get the host from a URL.
    
    Example: http://projecteuler.net/index.php?section=statistics => projecteuler.net"""
    p = urlparse(url)
    return p.netloc


def get_referrer_string(url):
    """We must use the referrer trick to download images from 4walled.org."""
    ref = ''
    if get_host(url) == '4walled.org':
        ref = '--referer=4walled.org'
        
    return ref


def get_file_name(url):
    """Return the file name from an URL.
       
    Ex.: http://example/pic.jpg => pic.jpg.
    """
    return os.path.split(urlparse(url)[2])[1]

#############################################################################

if __name__ == "__main__":
    pass