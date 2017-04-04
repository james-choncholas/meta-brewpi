SUMMARY = "A Qt5 development image"
HOMEPAGE = "http://www.jumpnowtek.com"
LICENSE = "MIT"

require console-image.bb

BREW_PKGS = " \
    vim \
    apache2 \
    fileoverlay \
"

IMAGE_INSTALL += " \
    ${BREW_PKGS} \
"

export IMAGE_BASENAME = "brewpi-image"
