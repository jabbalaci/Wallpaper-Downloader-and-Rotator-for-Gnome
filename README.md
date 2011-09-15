Wallpaper Downloader and Rotator for Gnome
==========================================

* Author:    Laszlo Szathmary (<jabba.laci@gmail.com>)
* Date:      April, 2011
* Last mod.: September, 2011
* Version:   0.6.0
* Website:   <https://ubuntuincident.wordpress.com/2011/04/06/wallpaper-downloader-and-rotator-for-gnome/>
* GitHub:    <https://github.com/jabbalaci/Wallpaper-Downloader-and-Rotator-for-Gnome>

This free software is copyleft licensed under the same terms as Python, or,
at your option, under version 2 of the GPL license.

(The original script was written by reddit user [iwakun](http://www.reddit.com/user/iwakun).
See the `original_by_iwakun/` folder for more information.)

The goal of this project is twofold. *First*, download images from a reddit (or wallbase.cc) category and 
store them in the file system. *Second*, rotate the downloaded images as wallpapers.

Here is the list of changes that I added to the original version:

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
* XML writing is done with the lxml library. (*deprecated*)
* Support for Flickr images (zioyero's patch).
* The URLs of the downloaded images are strored in an SQLite database.
  This way an already fetched image (either good or bad) won't be downloaded again.
* The script can set the produced XML as your wallpaper, you don't need to
  do that manually. Also, XML production can be switched off if you want to
  use a different wallpaper manager. (*deprecated*)

For installing lxml, please refer to [this entry][1], where the 
installation procedure is explained at the end of the post.

[1]: https://pythonadventures.wordpress.com/2011/04/04/write-xml-to-file/


Usage:
------

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

**New:**

I changed the default behaviour of the script. By default it doesn't
generate an XML output. I find it a better solution to use a dedicated
wallpaper manager for this task. Rotating the images with an XML is not 
very flexible, a wallpaper manager can provide a better experience.
To this end, I wrote a simple wallpaper rotator that does the job (see 
the file `02_wallpaper_rotator.py`).
If you still want the XML, set it in the config file.

*Warning!* The XML support is deprecated, I will remove that feature in a future version.


Managing the downloaded wallpapers:
-----------------------------------

There are several ways to manage the downloaded images:

1. The **new** way is to use `02_wallpaper_rotator.py`. Just launch it in the
   background. It uses the same config file as the wallpaper 
   downloader.
2. The old (and deprecated) way is to generate an XML and set it as your wallpaper.
   The downloader can do all that; for customizations see the config file.


Contributors:
-------------

* Nathan B, alias [ndbroadbent][2]
* Adrian Castillejos, alias [zioyero][3]

[2]: https://github.com/ndbroadbent
[3]: https://github.com/zioyero


Discussion:
-----------

Maybe I should remove the XML generator part from the downloader. After all, it's
"just" a downloader, so it should do just one thing. Since I made a wallpaper
changer, I don't use the XML any more. The new rotator script is preferred over
the XML, thus XML is sort of deprecated. *Update*: I will remove the XML support
in a future version.


TODO:
-----

1. Add support to the wallpaper site <http://4walled.org/>.

2. Add support to other operating systems: Windows, Mac.

