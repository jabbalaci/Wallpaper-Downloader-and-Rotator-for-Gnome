#!/usr/bin/env python

"""
Extract images from a 4walled.org page.
"""

import urllib2

from BeautifulSoup import BeautifulSoup


def get_jpg_image(soup):
    """Extract the URL of the JPG image from the HTML of a 4walled.org subpage."""
    image = None

    div = soup.find('div', {'id' : 'mainImage'})
    if div:
        a = div.find('a', href=True)
        if a:
            image = a['href']

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
    for tag in soup.findAll('li', {'class' : 'image'}):
        a = tag.find('a', href=True)
        if a:
            pages.append(a['href'])
        
    return pages


def get_image_url_list(url):
    """Controller function for getting the URLs of the JPG images."""
    soup = BeautifulSoup(urllib2.urlopen(url).read())
    
    subpages = get_subpages(soup)
    images = extract_images_from_pages(subpages)
    
    return images

#############################################################################

if __name__ == "__main__":
    url = 'http://4walled.org/search.php?tags=linux&board=&width_aspect=&searchstyle=larger&sfw=0&search=search'
    for url in get_image_url_list(url):
        print url
    