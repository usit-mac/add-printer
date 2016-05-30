add-printer
===========

This is a utility which creates an installable `pkg` that can be installed on
any OS X-client. It will add a printer to the system via `lpadmin`. The `ppd` is
included in the `pkg` which means that the client that installs the `pkg` does
not have to worry about installing driver packages and so on.

## Install

Install on your system with `setuptools`. It's always best to use the `--user`
flag to avoid permission issues.

```
$ cd add-printer
$ python setup.py install --user
```

## Using

Create a `pkg` by running `gen-printer-pkg` after installing the package.

```
$ gen-printer-pkg --name printer-name --displayname "A printer" --output-directory ./ --ppd /Library/Printers/PPDs/Contents/Resources/RICOH\ MP\ C401.gz
make -f Makefile -e pack-script-postinstall pack-RICOH\ MP\ C401.gz
******************************************************************

Using /usr/bin/pkgbuild, make sure scripts are
named preinstall/postinstall

Also check your pack-script-* stanzas in PAYLOAD

******************************************************************

Disabling bundle relocation.
If you need to override permissions or ownerships, override modify_packageroot in your Makefile
Creating /tmp/the_luggage/add_printer_printer-name-20160530/payload/add_printer_printer-name-20160530.pkg with /usr/bin/pkgbuild.
sudo /usr/bin/pkgbuild --root /tmp/the_luggage/add_printer_printer-name-20160530/root \
		--component-plist /tmp/the_luggage/add_printer_printer-name-20160530/luggage.pkg.component.plist \
		--identifier no.uio.usit.add_printer_printer-name \
		--filter "/CVS$" --filter "/\.svn$" --filter "/\.cvsignore$" --filter "/\.cvspass$" --filter "/(\._)?\.DS_Store$" --filter "/\.git$" --filter "/\.gitignore$" \
		--scripts /tmp/the_luggage/add_printer_printer-name-20160530/scripts \
		--version 20160530 \
		--ownership preserve --quiet \
		/tmp/the_luggage/add_printer_printer-name-20160530/payload/add_printer_printer-name-20160530.pkg
```

## Requirements

You need to have [the luggage](https://github.com/unixorn/luggage) for this to
work.
