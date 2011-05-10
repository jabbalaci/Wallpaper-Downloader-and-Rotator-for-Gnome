#!/usr/bin/env python

"""
Extract images from a reddit page.
"""

import urllib2

from BeautifulSoup import BeautifulSoup


def get_jpg_images(soup):
    """Extract the URLs of JPG images from the HTML of a reddit category. 
    
    This method doesn't extract Flickr images.
    """
    images = []

    for tag in soup.findAll('a', href=True):
        if tag['href'].lower().endswith('jpg'):
            if tag['href'] not in images:
                images.append(tag['href'])  # no duplicates and keep the order
                
    return images
# get_jpg_images


def get_flickr_images(soup):
    """Extract Flickr images."""
    flickr = []
    for tag in soup.findAll('a', href=True):
        if tag['href'].lower().endswith('photostream/'):
            if tag['href'] not in flickr:
                flickr.append(tag['href'])

    images = []
    for flickr_page in flickr:
        bs = BeautifulSoup(urllib2.urlopen(flickr_page).read())
        li = get_jpg_images(bs)
        if len(li) > 0:
            images.append(li[0])

    return images
# get_flickr_images


def get_image_url_list(url):
    """Controller function for getting the URLs of the JPG images."""
    soup = BeautifulSoup(urllib2.urlopen(url).read())
    
    list_1 = get_jpg_images(soup)
    list_2 = get_flickr_images(soup)
    
    union = []
    union.extend(list_1)
    union.extend(list_2)
    
    return union
# get_image_url_list
