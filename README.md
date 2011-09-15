Wallpaper Downloader and Rotator for Gnome
==========================================

* Author:    Laszlo Szathmary (<jabba.laci@gmail.com>)
* Date:      April, 2011
* Last mod.: September, 2011
* Version:   0.6.8
* Website:   <https://ubuntuincident.wordpress.com/2011/04/06/wallpaper-downloader-and-rotator-for-gnome/>
* GitHub:    <https://github.com/jabbalaci/Wallpaper-Downloader-and-Rotator-for-Gnome>

This free software is copyleft licensed under the same terms as Python, or,
at your option, under version 2 of the GPL license.

(The original script was written by reddit user [iwakun](http://www.reddit.com/user/iwakun).
See the `original_by_iwakun/` folder for more information.)

The goal of this project is twofold. *First*, download images from a wallpaper site.
*Second*, rotate the downloaded images as wallpapers.

Here is the list of changes that I added to the original version:

* **New!** XML support is dropped. For setting the images as
  wallpapers, use the script `02_wallpaper_rotator.py`.
* **New!** Support for [4walled.org](http://4walled.org) is added!
* **New!** Support for [wallbase.cc](http://wallbase.cc) is added!
* Large images can be resized to fit your screen resolution. By default,
  the maximum width of images can be 1920 pixels. You can customize it in the
  config file. It's recommended, this way the images will occupy much less space
  on your hard drive.
* You can specify several categories and the downloader will grab
  images from all these sites. The same is true for rotator: you can specify
  several categories and it will pick a random image from the whole list.
  See the config file for more details.
* The project includes an automatic wallpaper changer script
  called `02_wallpaper_rotator.py`. You don't need any third-party managers anymore.
* You can choose from several categories. You can also 
  specify your favorite category.
* Screen scraping is done with the BeautifulSoup library.
* The most important change is the filtering of images that are
  unsuitable as wallpapers, i.e. small images, portrait images, and
  images with strange ratio are removed from the list.
* Support for Flickr images (zioyero's patch).
* The URLs of the downloaded images are strored in an SQLite database.
  This way an already fetched image (either good or bad) won't be downloaded again.


Supported wallpaper sites
-------------------------

1. <http://www.reddit.com>
2. <http://wallbase.cc>
3. <http://4walled.org>


Usage
-----

First, you might want to customize some settings in the `config.py` file.
The most important thing is the `PHOTO_DIR` directory, i.e. where to store
the downloaded images. Create this directory if it doesn't exist.
Then, simply launch the script:

    ./01_wallpaper_downloader.py
    
You can also add it to your crontab:

    $ crontab -e
    10 */2 * * * /absolute_path_to/wallpaper_downloader.py
    
Add the second line to the end of the crontab list. Here the script is 
called at every two hours (at 0h10, 2h10, etc.).

For setting the images as wallpapers:

    ./02_wallpaper_rotator.py &
    
That is, just launch it in the background. It uses the same config file as 
the wallpaper downloader. I put it among my startup applications, thus it
starts automatically.


Contributors
------------

* Nathan B, alias [ndbroadbent][1]
* Adrian Castillejos, alias [zioyero][2]

[1]: https://github.com/ndbroadbent
[2]: https://github.com/zioyero


TODO
----

1. Add support to other operating systems: Windows, Mac.

2. Any ideas? Tell me!
