SUMMARY = "Copies files into the rootfs"
DESCRIPTION = "File copier"
HOMEPAGE = ""
LICENSE = "CLOSED"

inherit allarch


# checkout this link for info, and helpful definitions for environment variables
# http://stackoverflow.com/questions/34067897/bitbake-not-installing-my-file-in-the-rootfs-image


SRC_URI = "                        \
    file://BREW.py                 \
    file://HardwareUtility.py      \
    file://PIDBrewLoop.py          \
    file://PID.py                  \
    file://README.txt              \
    file://static/g.line-min.js    \
    file://static/g.raphael-min.js \
    file://static/raphael-min.js   \
    file://static/style.css        \
    file://templates/BrewMe.html   \
    file://Test/GPIOTest.py        \
    "

do_install() {

    install -d ${D}/brewpi
    install -d ${D}/brewpi/static
    install -d ${D}/brewpi/templates
    install -d ${D}/brewpi/Test
 
    install -m 0755 ${WORKDIR}/BREW.py                  ${D}/brewpi/
    install -m 0755 ${WORKDIR}/HardwareUtility.py       ${D}/brewpi/
    install -m 0755 ${WORKDIR}/PIDBrewLoop.py           ${D}/brewpi/
    install -m 0755 ${WORKDIR}/PID.py                   ${D}/brewpi/
    install -m 0755 ${WORKDIR}/README.txt               ${D}/brewpi/
    install -m 0755 ${WORKDIR}/static/g.line-min.js     ${D}/brewpi/static/
    install -m 0755 ${WORKDIR}/static/g.raphael-min.js  ${D}/brewpi/static/
    install -m 0755 ${WORKDIR}/static/raphael-min.js    ${D}/brewpi/static/
    install -m 0755 ${WORKDIR}/static/style.css         ${D}/brewpi/static/
    install -m 0755 ${WORKDIR}/templates/BrewMe.html    ${D}/brewpi/templates/
    install -m 0755 ${WORKDIR}/Test/GPIOTest.py         ${D}/brewpi/Test/


    # at some point try doing something like this... xilinx does it
    #for DTB_FILE in `ls *.dtb *.dtbo`; do
    #    install -Dm 0644 ${B}/${DTB_FILE} ${DEPLOYDIR}/${DTB_FILE}
    #done

    # below command copies everything in directory, but not recursive
    #cp -dr --no-preserve=ownership ${THISDIR}/files/* ${D}/brewpi
    
    #install -d ${D}/brewpi #create the destination directory (that's #{D})
    #install -m 755  ${THISDIR}/files/the_files

    #install -m 0644 ${MY_FILES} ${D}/brewpi

    #rsync -r ${THISDIR}/files/* ${D}/brewpi

    #for f in ${HOME}/Projects/poky-morty/meta-brewpi/recipes-brew/fileoverlay/files/*; do \
    #    install -D -t ${D}/brewpi $$f; \
    #done
}

FILES_${PN} += "                    \
    /brewpi/BREW.py                 \
    /brewpi/HardwareUtility.py      \
    /brewpi/PIDBrewLoop.py          \
    /brewpi/PID.py                  \
    /brewpi/README.txt              \
    /brewpi/static/g.line-min.js    \
    /brewpi/static/g.raphael-min.js \
    /brewpi/static/raphael-min.js   \
    /brewpi/static/style.css        \
    /brewpi/templates/BrewMe.html   \
    /brewpi/Test/GPIOTest.py        \
    "
