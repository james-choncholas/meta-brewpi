#!/usr/bin/env bash

############### One time setup ###################

# Built on Ubuntu 16.0.4

#Reference guide:
#See http://www.jumpnowtek.com/rpi/Raspberry-Pi-Systems-with-Yocto.html


#Download the following packages: (some aren't neccessary) lol
packages="\
    build-essential \
    chrpath \
    diffstat \
    gawk \
    git \
    libncurses5-dev \
    pkg-config \
    subversion \
    texi2html \
    texinfo \
    python2.7 \
"
sudo apt-get update

echo "installing packages..."
sudo apt-get install $packages

# Start work in the following directory
# NOTE : if you have problems later, check permissions of folders
# as well as if the drive is mounted with the exec flag. Drive mounting
# flags may have to be changed in fstab or udev.
MYPATH=/media/jim/Data/Projects
MYIP=https://github.com/james-choncholas
mkdir -p $MYPATH/yocto

# Clone my clone of the Yacto poky repository (morty branch):
cd $MYPATH/yocto
git clone -b morty $MYIP/poky-morty

# Clone the following repositories inside the poky repo you just cloned:
cd $MYPATH/yocto/poky-morty
git clone -b morty $MYIP/meta-openembedded
git clone -b morty $MYIP/meta-qt5
git clone -b morty $MYIP/meta-raspberrypi

# Clone the application code repo
cd $MYPATH/
git clone -b master $MYIP/meta-brewpi

# Create the build directory and link to config files:
mkdir -p $MYPATH/build/conf
cp $MYPATH/meta-brewpi/conf/bblayers.conf $MYPATH/build/conf
cp $MYPATH/meta-brewpi/conf/local.conf $MYPATH/build/conf

exit 0
