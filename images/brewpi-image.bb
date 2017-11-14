SUMMARY = "A Qt5 development image"
HOMEPAGE = "http://www.jumpnowtek.com"
LICENSE = "MIT"

require console-image.bb

BREW_PKGS = " \
    vim \
    freerdp \
    python-flask \
    rpi-gpio \
    fileoverlay \
    boot-script \
"

IMAGE_INSTALL += " \
    ${BREW_PKGS} \
"

export IMAGE_BASENAME = "brewpi-image"
