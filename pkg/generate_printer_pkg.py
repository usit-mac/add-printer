#!/usr/bin/env python
import sys
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--name', required=True, help="Name of the printer")
    parser.add_argument('--location', default="No specific loacation",)
    parser.add_argument('--ppd', required=True,help="Path to PPD file") 

    args = parser.parse_args()

    with open('Makefile', 'r') as infile:
	with open('Makefile-out', 'w') as ofile:
	   ofile.write(infile.read().replace('__PPDFILE__', args.ppd))

    with open('postinstall', 'r') as infile:
	content_str=infile.read()

	content_str= content_str.replace('__NAME__',args.name)	
	content_str= content_str.replace('__LOCATION__',args.location)
	content_str= content_str.replace('__PPD__',args.ppd)

	with open('postinstall-out','w') as ofile:
	    ofile.write(content_str)
