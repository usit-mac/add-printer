#!/usr/bin/env python
import argparse
import subprocess

_LPADMIN = '/usr/sbin/lpadmin'

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--name', required=True, help="Name of a printer")
    parser.add_argument('--ppd', reauired=True, help="Path to PPD file")
    parser.add_argument('--location', default="No specific location", help="Printer location")

    args = parser.parse_args()

    base_url = "smb://pushprint.uio.no/"
    url = base_url + args.name

    subprocess.check_call([_LPADMIN, "-p", args.name, "-L", args.location, "-v", url, "-P", args.ppd])
