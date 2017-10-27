# Brewcifier
   
To build the Brewcifier code from scratch, START HERE!!!
Built on Ubuntu 16.0.4
<br><br>
Reference guide:
See http://www.jumpnowtek.com/rpi/Raspberry-Pi-Systems-with-Yocto.html
<br><br>
## One time setup

Before running install.sh modify the file to set
the install location and the git repo location.

After running install.sh you should see the following
directory structure.
<br><br>
Reference folder structure:   
Projects/   
  yacto/   
    poky-morty/   
      meta-openembedded/   
      meta-qt5/   
      ...   
    meta-brewpi/   
    build/   
      conf/   

## Build and Deploy

### Run the build:
cd $MYPATH
source poky-morty/oe-init-build-env
bitbake brewpi-image


### Copy to the SD card:
find the card using lsblk
cd ~/Projects/poky-morty/meta-brewpi/scripts
sudo ./mk2parts.sh mmcblk0
sudo mkdir /media/card
export OETMP=${HOME}/Projects/build/tmp
export MACHINE=raspberrypi
./copy_boot.sh mmcblk0
./copy_rootfs.sh mmcblk0 brewpi


## Notes and Tools

The user name of the raspberry pi is root
<br><br>
### To see list of available packages for adding to image file:
cd $MYPATH
source poky-morty/oe-init-build-env
bitbake -s

### To clean the image
cd $MYPATH   
source poky-morty/oe-init-build-env   
bitbake -c clean brewpi-image   

### To build for raspberry pi 2 v1.2 model B:
Change the MACHINE variable in meta-brewpi/conf/local.conf to "raspberrypi"   
When copyping to the SD card, export MACHINE="raspberrypi"   

### To build for raspberry pi 3:
Change the MACHINE variable in meta-brewpi/conf/local.conf to "raspberrypi2"   
When copyping to the SD card, export MACHINE="raspberrypi2"   

## Debugging 

### Once a bunch of python packages (python-flask, python-werkzeug ...) didn't build
Error was "ERROR: oe_runmake failed"   
The solution was to run bitbake -c cleanall <python-flask>   
<br>
<br>
Note: most of the custom recipes exist in the recipes-brewpi but not all...   
<br>
<br>
### Apache errors 
In $MYPATH/poky-morty/meta-openembedded/meta-webserver/recipes-httpd/apache2
change the two apache .bb files. The SRC_URI variable needs to use an archived
version of apache. This is probably done by appending "archive." to the url.
For example SRC_URI = "http://archive.apache.org/..."
<br>
<br>
### Disk notes 
Make sure your disk has been mounted with the exec flag. Check fstab or udev
<br>
<br>



## This layer depends on:

    URI: git://git.yoctoproject.org/poky.git
    branch: morty
    revision: HEAD
    commit: 6c08cf2

    URI: git://git.openembedded.org/meta-openembedded
    branch: morty
    revision: HEAD
    commit: fe5c833

    URI: https://github.com/meta-qt5/meta-qt5.git
    branch: morty
    revision: HEAD
    commit: 3601fd2

    URI: git://git.yoctoproject.org/meta-raspberrypi 
    branch: morty
    revision: HEAD
    commit: cce6292

    meta-rpi layer maintainer: Scott Ellis <scott@jumpnowtek.com>
