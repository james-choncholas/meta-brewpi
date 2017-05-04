SUMMARY = "Copies files into the rootfs"
DESCRIPTION = "File copier"
HOMEPAGE = ""
LICENSE = "CLOSED"

inherit allarch

do_install() {

    # This works
    install -d ${D}/brewpi
    cp -dr --no-preserve=ownership ${THISDIR}/files/* ${D}/brewpi

    
    # At some point you should try using install to make sure file's permissions are correct
    #  but install cannot be used recursively
    # checkout this link for info, and helpful definitions for environment variables
    # http://stackoverflow.com/questions/34067897/bitbake-not-installing-my-file-in-the-rootfs-image
    #install -d ${D}/brewpi #create the destination directory (that's #{D})
    #install -m 755  ${THISDIR}/files/the_files


    # Shit that didn't work
    
    #install -m 0644 ${MY_FILES} ${D}/brewpi

    #rsync -r ${THISDIR}/files/* ${D}/brewpi

    #for f in ${HOME}/Projects/poky-morty/meta-brewpi/recipes-brew/fileoverlay/files/*; do \
    #    install -D -t ${D}/brewpi $$f; \
    #done
}

FILES_${PN} += "/brewpi"
