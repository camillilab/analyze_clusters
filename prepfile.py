#! usr/bin/env python

"""
This script is used to convert the SOR and sCLIP bash output files from reads_analysis.sh
into proper, headed .csv files.

Usage:

Place SOR.txt and sCLIP.txt into the same directory as prepfile.py

Open the terminal or otherwise execute

>> python prepfile.py

The output files SOR.csv and sCLIP.csv should output in the current directory

Author: Jacob Bourgeois
Email: jacob.bourgeois@tufts.edu
Organization: Tufts Sackler School of Biomedical Sciences; Camilli Lab

License: 3-clause BSD


"""

import os
import csv


def fix_file(input_file, output_file):

    # create csv writer object
    with open(output_file, 'w') as o:
        writer = csv.writer(o)

        # write header
        writer.writerow(('COLOR', 'POS', 'CIGAR', 'TLEN'))

        # open input txt file
        with open(input_file, 'r') as i:
            for line in i:
                # split line on spaces
                data = line.split(' ')
                # write data into csv file
                writer.writerow(data)
    return


def main():
    # Define current working directory and files
    cwd = os.getcwd()
    SOR_input = os.path.join(cwd, 'SOR.txt')
    SOR_output = os.path.join(cwd, 'acc_sor.csv')
    sCLIP_input = os.path.join(cwd, 'sCLIP.txt')
    sCLIP_output = os.path.join(cwd, 'acc_sclip.csv')

    # check to make sure the files are there
    if not SOR_input:
        print("Error! SOR.txt was not found.")
        quit()

    if not sCLIP_input:
        print("Error! sCLIP.txt was not found.")
        quit()

    # convert files to proper csv format with headers
    print("Fixing SOR.txt...")
    fix_file(SOR_input, SOR_output)

    print("Fixing sCLIP.txt...")
    fix_file(sCLIP_input, sCLIP_output)

    print("Done! Rename these files with the proper reference accession number and place them in the SOR and sCLIP"
          "folders respectively ie. FN545816_sclip.csv and FN545816_sor.csv.")


# make executable
if __name__ == "__main__":
    main()
