#!/usr/bin/env python

"""
Extract images from a wallbase.cc page.
"""

import urllib2

from BeautifulSoup import BeautifulSoup


def get_jpg_image(soup):
    """Extract the URL of the JPG image from the HTML of a wallbase.cc subpage."""
    image = None

    div = soup.find('div', {'id' : 'bigwall', 'class' : 'right'})
    if div:
        img = div.find('img', src=True)
        if img:
            image = img['src']

    return image


def extract_images_from_pages(pages):
    """Extract images from subpages."""
    li = []
    for page in pages:
        soup = BeautifulSoup(urllib2.urlopen(page).read())
        image = get_jpg_image(soup)
        li.append(image)
        
    return [x for x in li if x]     # remove None elems


def get_subpages(soup):
    """Images can be found on separate pages. Extract the URL of these subpages."""
    pages = []
    for tag in soup.findAll('a', {'class' : 'thdraggable thlink', 'target' : '_blank'}):
        pages.append(tag['href'])
        
    return pages


def get_image_url_list(url):
    """Controller function for getting the URLs of the JPG images."""
    soup = BeautifulSoup(urllib2.urlopen(url).read())
    
    subpages = get_subpages(soup)
    images = extract_images_from_pages(subpages)
    
    return images

#############################################################################

if __name__ == "__main__":
    url = 'http://wallbase.cc/tags/info/7964'
    for url in get_image_url_list(url):
        print url
    