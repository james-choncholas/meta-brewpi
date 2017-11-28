#!/bin/bash

LOG_PATH="/var/log/network.log"
now=$(date +"%m-%d %r")

iface='wlan0'
pingip='google.com'

/bin/ping -c 2 -I $iface $pingip > /dev/null 2> /dev/null
if [ $? -ge 1 ] ; then
	echo "$now Network is DOWN. restarting" >> $LOG_PATH
	/sbin/ifdown $iface
	sleep 5
	/sbin/ifup -f $iface
fi
