#!/usr/bin/env python

import argparse
import subprocess

parser = argparse.ArgumentParser()

parser.add_argument('-p','--printerName',default= "test-printer", help ="Name of a printer")
parser.add_argument('-P','--ppd_path',default = "/Library/Printers/PPDs/Contents/Resource/HP\ LaserJet\ 600\ M601\ M602\ M603.gz", help="Path to PPD files")
parser.add_argument('-L','--location',default="usit_1340",help ="Printer location")

args = parser.parse_args()

url = "smb://pushprint.uio.no"
PATH = url + args.printerName

subprocess.check_call(["lpadmin","-p", args.printerName, "-L", args.location, "-v", PATH, "-P", args.ppd_path, "-L", args.location])
