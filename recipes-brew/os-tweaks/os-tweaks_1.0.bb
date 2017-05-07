SUMMARY = "Set up OS for brewing"
DESCRIPTION = "Set up OS config files to start BREW.py on boot and use GPIO overlay for temperature sensor"
HOMEPAGE = ""
LICENSE = "CLOSED"

inherit allarch

do_install() {

    # setup temperature sensor(s?)    
    #echo "dtoverlay=w1-gpio,gpiopin=21" >> ${D}/boot/config.txt

    # add the wifi password :)
    #echo "
    #network={
    #    key_mgmt=WPA-PSK
    #    ssid="Brewcifier"
    #    psk="brewmebro"
    #}
    #" >> ${D}/etc/wpa_supplicant.conf
}

#FILES_${PN} += "/etc/wpa_supplicant.conf"
