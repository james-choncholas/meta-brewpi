SUMMARY = "Set up OS for brewing"
DESCRIPTION = "Set up OS config files to start BREW.py on boot and use GPIO overlay for temperature sensor"
HOMEPAGE = ""
LICENSE = "CLOSED"

inherit allarch

do_install() {

    # setup temperature sensor(s?)    
    echo "dtoverlay=w1-gpio,gpiopin=21" >> ${D}/boot/config.txt

    # add the wifi password :)
    #network={
    #    key_mgmt=WPA-PSK
    #    ssid="<ssid>"
    #    psk="<passphrase>"
    #}

}

#FILES_${PN} += "/brewpi"
