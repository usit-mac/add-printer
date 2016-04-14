include /usr/local/share/luggage/luggage.make

TITLE=setup_add_printer
VERSION=1.0
REVERSE_DOMAIN=no.uio.usit
PPD=ppd_test.gz
THEDIR=${WORK_D}/Library/Printers/PPDs/Contents/Resources

PAYLOAD=\
	pack-script-postinstall\
	pack-${PPD}

pack-${PPD}:
	@sudo mkdir -p ${THEDIR}
	@sudo chown root:wheel ${THEDIR}
	@sudo chmod 755 ${THEDIR}
	@sudo ${CP} ./${PPD} ${THEDIR}
	@sudo chown root:wheel ${THEDIR}/${PPD}
	@sudo chmod 755 ${THEDIR}/${PPD}
