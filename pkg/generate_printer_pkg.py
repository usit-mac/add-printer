#!/usr/bin/env python
import sys
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--name', required=True, help="Name of the printer")
    parser.add_argument('--location', default="No specific loacation",)
    parser.add_argument('--ppd', required=True,help="Path to PPD file") 

    args = parser.parse_args()

    with open('Makefile-template', 'r') as infile:
	with open('Makefile', 'w') as ofile:
	   ofile.write(infile.read().replace('__PPDFILE__', args.ppd))

    with open('postinstall', 'r') as infile:
	with open('postinstall-out','w') as ofile:
	    ofile.write(infile.read().replace('__NAME__',args.name))
	    ofile.write(infile.read().replace('__LOCATION__',args.location))	
            ofile.write(infile.read().replace('__PPD__',args.ppd))
