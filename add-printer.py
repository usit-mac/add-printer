#!/usr/bin/env python

import argparse
import subprocess

parser = argparse.ArgumentParser()

parser.add_argument('-p','--printer-name',default= "test-printer", help ="Name of a printer")
parser.add_argument('-v','--device-url',default ="smb://pushprint.uio.no/", help ="Print device URL")
parser.add_argument('-P','--ppd-path',default = "/Library/Printers/PPDs/Contents/Resource/HP LaserJet 600 M601 M602 M603.gz", help="Path to PPD files")
parser.add_argument('-L','--location',default="usit_1340",help ="Printer location")

args = parser.parser_args()

PATH = args.device-url + args.printer-name

subprocess.check_call(["lpadmin","-p args.printer-name", "-L args.location", "-v PATH", "-P args.ppd-path", "-L pars.location])


