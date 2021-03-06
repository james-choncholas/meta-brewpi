# Brewcifier

This is my take on the BrewPi - an automated, PID controlled, electronic beer brewing system.
<br><br>
See it in action: https://youtu.be/udd92xAymgw
<br><br>
Inputs: A one-wire temperature sensor   
Outputs: Two GPIO pins that toggle high and low to simulate button presses on a voltage regulator. 
The voltage regulator is connected to a heating element which heats the beer.
<br><br>

## Software Architecture
This repository is a layer in a yocto open embedded system. Yocto is tool to create custom linux distributions.
This layer adds required packages and configuration files to the poky-morty open embedded distribution
as well as application level code. This repository was forked from https://github.com/jumpnow/meta-rpi.
The Python scripts that control the beer brewing process live in the folder `recipes-brew/fileoverlay/files`
   
## One time setup

Built on Ubuntu 16.0.4
<br><br>
Reference guide: <br>
See http://www.jumpnowtek.com/rpi/Raspberry-Pi-Systems-with-Yocto.html
<br><br>

Get the install script with 
```
wget http://.../Brewcifier/meta-brewpi/raw/master/install.sh
```
<br><br>
Before running install.sh modify the file to set
the install location and the git repo location.
<br><br>
Be sure the top level directory is on an ext4 filesystem.
NTFS does not work.
<br><br>
After running install.sh you should see the following
directory structure.
```
Projects/   
  yacto/   
    poky-morty/   
      meta-openembedded/   
      meta-qt5/   
      ...   
    meta-brewpi/   
    build/   
      conf/   
```
<br><br>
## Build and Deploy

### Run the build:
```
cd $MYPATH
source yocto/poky-morty/oe-init-build-env
bitbake brewpi-image
```



### Copy to the SD card:
use `lsblk` to find the SD card. Update the location in $MYPATH/meta-brewpi/scripts/copyToSd.sh
```
cd $MYPATH/meta-brewpi/scripts
./copyToSd.sh
```

## Notes and Tools

The user name of the raspberry pi is root
<br><br>
### To see list of available packages for adding to image file:
```
cd $MYPATH
source poky-morty/oe-init-build-env
bitbake -s
```
<br>
### To clean the image
```
cd $MYPATH   
source poky-morty/oe-init-build-env   
bitbake -c clean brewpi-image   
```
<br>

### To build for raspberry pi 2 v1.2 model B:
Change the MACHINE variable in meta-brewpi/conf/local.conf to "raspberrypi"
<br><br>
When copyping to the SD card, export MACHINE="raspberrypi"   
<br><br>
### To build for raspberry pi 3:
Change the MACHINE variable in meta-brewpi/conf/local.conf to "raspberrypi2"
<br><br>
When copyping to the SD card, export MACHINE="raspberrypi2"
<br><br>

## Debugging 

### Once a bunch of python packages (python-flask, python-werkzeug ...) didn't build
Error was "ERROR: oe_runmake failed"   
The solution was to run bitbake -c cleanall \<python-flask\>   
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

