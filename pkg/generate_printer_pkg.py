#!/usr/bin/env python
import sys
import argparse
import os
from os.path import join
import shutil
import subprocess

_MAKE = '/usr/bin/make'

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--name', required=True, help="Name of the printer")
    parser.add_argument('--location', default="No specific loacation",)
    parser.add_argument('--ppd', required=True,help="PPD file") 
    parser.add_argument('--output-directory', required=True,help="Path to PPD file") 

    args = parser.parse_args()
   
    if not os.path.exists(args.output_directory):
	os.makedirs(args.output_directory)
	
    # If in same directory, don't copy
    if not os.path.join('.',args.ppd) == os.path.join(args.output_directory, args.ppd):
        shutil.copy(args.ppd,args.output_directory)
	
    with open('Makefile-template', 'r') as infile:
	content_str=infile.read()
	
    content_str = content_str.replace('__PPDFILE__',args.ppd)
    content_str = content_str.replace('__ADDPRINTER__',args.name)

    with open(os.path.join(args.output_directory,'Makefile'), 'w') as ofile:
	 ofile.write(content_str)

    with open('postinstall-template', 'r') as infile:
	content_str=infile.read()

    content_str = content_str.replace('__NAME__',args.name)	
    content_str = content_str.replace('__LOCATION__',args.location)
    content_str = content_str.replace('__PPD__',args.ppd)

    with open(os.path.join(args.output_directory,'postinstall'), 'w') as ofile:
        ofile.write(content_str)

    subprocess.check_call([_MAKE, "pkg", "-C", args.output_directory])

    os.remove(os.path.join(args.output_directory,'Makefile'))
    os.remove(os.path.join(args.output_directory,'postinstall'))

    if not os.path.join('.',args.ppd) == os.path.join(args.output_directory, args.ppd):
        os.remove(os.path.join(args.output_directory,args.ppd))
