Wallpaper Downloader and Rotator for Gnome
==========================================

* Authors:
    - Laszlo Szathmary (<jabba.laci@gmail.com>)
    - iwakun (<http://www.reddit.com/user/iwakun>)
* Date:      April, 2011
* Last mod.: May, 2011
* Version:   0.3.5
* Website:   <https://ubuntuincident.wordpress.com/2011/04/06/wallpaper-downloader-and-rotator-for-gnome/>
* GitHub:    <https://github.com/jabbalaci/Wallpaper-Downloader-and-Rotator-for-Gnome>

This free software is copyleft licensed under the same terms as Python, or,
at your option, under version 2 of the GPL license.

(The original script was written by reddit user iwakun.
See the `original_by_iwakun/` folder for more information.)

The goal of the script is to download images from a reddit category and 
create an XML file that can be set as background in Gnome. The XML file
will rotate the images.

Here is the list of changes that I added to the original version:

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


Contributors:
-------------

* Nathan B, alias ndbroadbent
* Adrian Castillejos, alias zioyero


Managing the downloaded wallpapers:
-----------------------------------

There are several ways to manage the downloaded images:

1. The easiest way is to let this job done by the script. By default,
   it produces an XML file and sets it as your wallpaper. See the
   config file if you want to do some customizations.
2. You can also use a wallpaper manager. I have already used wally but
   I had problems with it under Unity. It creates a system tray icon 
   but under Unity it's not visible so I couldn't use it...
   Nathan B, alias ndbroadbent suggests Cortina. Here is what he has to say 
   about it:

> I'd just like to mention that I found the 'Cortina' application, and it blows away Gnome's wallpaper rotater.
> It monitors an image directory and changes your wallpapers after a desired interval, but also:
> 
> * Can be set to change wallpapers in a random order
> * Puts an icon in the system tray
>     * Left-click: immediately change the wallpaper
>     * Right-click  => Current Wallpaper => remove from disk
> 
> You can install it from a custom PPA with this command:
> 
>     sudo add-apt-repository ppa:cs-sniffer/cortina && sudo apt-get update && sudo apt-get install cortina

I couldn't install Cortina under Ubuntu 11.04 but it might work with older systems.
Note that wally can do similar things too.

