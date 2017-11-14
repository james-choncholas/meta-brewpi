#!/bin/bash

sudo ./mk2parts.sh mmcblk0
sudo mkdir /media/card

export OETMP=../../build/tmp/
export MACHINE=raspberrypi

./copy_boot.sh mmcblk0
./copy_rootfs.sh mmcblk0 brewpi

sync & sync
