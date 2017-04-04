SUMMARY = "Copies files into the rootfs"
DESCRIPTION = "File copier"
HOMEPAGE = ""
LICENSE = "CLOSED"

inherit allarch

do_install() {

install -d ${D}/brewpi
cp -dr --no-preserve=ownership ${THISDIR}/files/* ${D}/brewpi

# shit that didn't work
# install -m 0644 ${MY_FILES} ${D}/brewpi
# rsync -r ${THISDIR}/files/* ${D}/brewpi
#for f in ${HOME}/Projects/poky-morty/meta-brewpi/recipes-brew/fileoverlay/files/*; do \
#    install -D -t ${D}/brewpi $$f; \
#done
}

FILES_${PN} += "/brewpi"
