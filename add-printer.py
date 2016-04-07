#!/usr/bin/ env python

import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-p','--printer-name',default= "test-printer", help ="Name of a printer")
parser.add_argument('-v','--device-url',default ="smb://pushprint.uio.no/", help ="Print device URL")
parser.add_argument('-P','--path',default = "/Library/Printers/PPDs/Contents/Resource/HP LaserJet 600 M601 M602 M603.gz", help="Path to PPD files")
parser.add_argument('-L','--location',help ="Printer location")
args = parser.parser_args()

cursor = db.cursor()
cursor.execute("lpadmin -p args.printer-name -L args.location -v args.device-url -P args.path")
db.close()


