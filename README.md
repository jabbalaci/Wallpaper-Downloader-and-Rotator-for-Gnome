Wallpaper Downloader and Rotator for Gnome
==========================================

* Author:    Laszlo Szathmary (<jabba.laci@gmail.com>)
* Date:      April, 2011
* Last mod.: June, 2011
* Version:   0.4.0
* Website:   <https://ubuntuincident.wordpress.com/2011/04/06/wallpaper-downloader-and-rotator-for-gnome/>
* GitHub:    <https://github.com/jabbalaci/Wallpaper-Downloader-and-Rotator-for-Gnome>

This free software is copyleft licensed under the same terms as Python, or,
at your option, under version 2 of the GPL license.

(The original script was written by reddit user [iwakun](http://www.reddit.com/user/iwakun).
See the `original_by_iwakun/` folder for more information.)

The goal of the script is to download images from a reddit category and 
create an XML file that can be set as background in Gnome. The XML file
will rotate the images.

Here is the list of changes that I added to the original version:

* **New!** The project includes an automatic wallpaper changer script
  called `changer.py`. You don't need any third-party managers anymore.
* You can choose from several reddit categories. You can also 
  specify your favorite category.
* Screen scraping is done with the BeautifulSoup library.
* The most important change is the filtering of images that are
  unsuitable as wallpapers, i.e. small images, portrait images, and
  images with strange ratio are removed from the list.
* XML writing is done with the lxml library.
* Support for Flickr images (zioyero's patch).
* The URLs of the downloaded images are strored in an SQLite database.
  This way an already fetched image (either good or bad) won't be downloaded again.
* The script can set the produced XML as your wallpaper, you don't need to
  do that manually. Also, XML production can be switched off if you want to
  use a different wallpaper manager.

For installing lxml, please refer to [this entry][1], where the 
installation procedure is explained at the end of the post.

[1]: https://pythonadventures.wordpress.com/2011/04/04/write-xml-to-file/


Usage:
------

First, you might want to customize some settings in the `config.py` file.
The most important thing is the `PHOTO_DIR` directory, i.e. where to store
the downloaded images. Create this directory if it doesn't exist.
Then, simply launch the script:

    ./wallpapers.py
    
You can also add it to your crontab:

    $ crontab -e
    10 */2 * * * /absolute_path_to/wallpapers.py
    
Add the second line to the end of the crontab list. Here the script is 
called at every two hours (at 0h10, 2h10, etc.).

**New:**

I changed the default behaviour of the script. By default it doesn't
generate an XML output. I find it a better solution to use a dedicated
wallpaper manager for this task. Rotating the images with an XML is not 
very flexible, a wallpaper manager can provide a better experience.
To this end, I wrote a simple wallpaper rotator that does the job (see 
the file `changer.py`).
If you still want the XML, set it in the config file.


Managing the downloaded wallpapers:
-----------------------------------

There are several ways to manage the downloaded images:

1. The **new** way is to use `changer.py`. Just launch it in the
   background. It uses the same config file as the wallpaper 
   downloader.
2. The old way is to generate an XML and set it as your wallpaper.
   The downloader can do all that; for customizations see the config file.


Contributors:
-------------

* Nathan B, alias [ndbroadbent][2]
* Adrian Castillejos, alias [zioyero][3]

[2]: https://github.com/ndbroadbent
[3]: https://github.com/zioyero


TODO:
-----

1. Add support to more wallpaper sites: <http://wallbase.cc>, <http://4walled.org/>.

2. Huge images (typically from `/r/SpacePorn`) should be resized to a reasonable size.
   It could be done with PIL. Example:

        from PIL import Image
        import glob, os
    
        size = 128, 128
    
        for infile in glob.glob("*.jpg"):
            file, ext = os.path.splitext(infile)
            im = Image.open(infile)
            im.thumbnail(size, Image.ANTIALIAS)
            im.save(file + ".thumbnail", "JPEG")

3. Currently the downloader grabs images from one site only,
   this is specified by the user in the config file. It'd be nice if the
   downloader could visit _several_ or even _all_ the sites that are listed
   in the config file. This way if I want to see wallpapers from another
   category, that category would already contain lots of images.
