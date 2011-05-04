#!/usr/bin/env python

"""
Database handler.

Downloaded images (either good or bad) are stored in an SQLite database.
This way, an already fetched image won't be downloaded again.
"""

import os
import sqlite3
import atexit


SQLITE_DB = None

SCHEMA = """
-- Schema for the wallpapers.

CREATE TABLE "images" (
    "image_url" TEXT PRIMARY KEY  NOT NULL,
    "good_as_wallpaper" INTEGER NOT NULL  DEFAULT 1,
    "fetched_on" DATETIME NOT NULL  DEFAULT (datetime('now','localtime'))
)
"""

conn = None


def is_image_in_db(url):
    """Determine if an image URL is in the DB or not."""
    query = "SELECT COUNT(*) FROM images WHERE image_url='{0}'".format(url)
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result[0][0] > 0


def add_image(url, good=True):
    """Insert an image URL in the DB."""
    good = 1 if good else 0
    query = "INSERT INTO images (image_url, good_as_wallpaper) VALUES ('{0}', {1})".format(url, good)
    try:
        conn.execute(query)
    except sqlite3.IntegrityError:
        print "# the image {0} is already in the DB...".format(url)


def create_db():
    """Create the DB if not exists."""
    global conn
    dir_name= os.path.split(SQLITE_DB)[0]
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    conn = sqlite3.connect(SQLITE_DB)
    conn.executescript(SCHEMA)


def init(sqlite_db):
    """Initialize the DB."""
    global SQLITE_DB, conn
    atexit.register(close)
    SQLITE_DB = sqlite_db
    
    if not os.path.exists(SQLITE_DB):
        create_db()
    if not conn:
        conn = sqlite3.connect(SQLITE_DB)
        
        
def close():
    """Commit and close DB connection.
    
    As I noticed, commit() must be called, otherwise changes
    are not commited automatically when the program terminates.
    """
    if conn:
        conn.commit()
        conn.close()
        

if __name__ == "__main__":
    # some simple tests: 
    #init('/trash/gnome-wallpapers/database/wallpapers.sqlite')
    #img = 'http://example.com/1.jpg'
    #print is_image_in_db(img)
    #add_image(img)
    #print is_image_in_db(img)
    pass
