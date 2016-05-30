#!/usr/bin/env python
import sys
import argparse
import os
import os.path as op
import shutil
import subprocess

_MAKE = '/usr/bin/make'

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--name', required=True, help="Name of the printer")
    parser.add_argument('--displayname', type=str)
    parser.add_argument('--location', default="No specific loacation",)
    parser.add_argument('--ppd', required=True,help="PPD file") 
    parser.add_argument('--protocol', type=str, default='smb')
    parser.add_argument('--server', type=str, default='pushprint.uio.no')
    parser.add_argument('--output-directory', required=True,help="Path to PPD file") 

    args = parser.parse_args()

    name = args.name.replace(' ', '_').lower()
    ppd = op.basename(args.ppd)

    if not os.path.exists(args.output_directory):
        os.makedirs(args.output_directory)

    # If in same directory, don't copy
    if not ppd in os.listdir(args.output_directory):
        shutil.copy(args.ppd, args.output_directory)

    with open('Makefile-template', 'r') as infile:
        content_str = infile.read()

    content_str = content_str.replace('__PPDFILE__', ppd.replace(' ', '\ '))
    content_str = content_str.replace('__PRINTERNAME__', name)

    with open(os.path.join(args.output_directory,'Makefile'), 'w') as ofile:
        ofile.write(content_str)

    with open('postinstall-template', 'r') as infile:
        content_str = infile.read()

    content_str = content_str.replace('__NAME__', name)
    content_str = content_str.replace('__LOCATION__', args.location)
    content_str = content_str.replace('__PPD__', ppd)
    content_str = content_str.replace('__PROTOCOL__', args.protocol)
    content_str = content_str.replace('__SERVER__', args.server)

    if args.displayname:
        content_str = content_str.replace('__INFO__', args.displayname)

    with open(os.path.join(args.output_directory,'postinstall'), 'w') as ofile:
        ofile.write(content_str)

    try:
        subprocess.check_call(['sudo', _MAKE, "pkg", "-C", args.output_directory])
    except Exception as e:
        print "Make failed with\n  %s" % str(e)

    os.remove(op.join(args.output_directory,'Makefile'))
    os.remove(op.join(args.output_directory,'postinstall'))
