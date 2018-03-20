README for Camilli Laboratory's Genome-Wide Detection of Conservative Site-Specific Recombination in Bacteria

This is a series of scripts that extracts same-orientation reads (SOR) and 5'-clipped 
reads (sCLIP) from sequencing data and analyzes the patterns for detection of potential 
inversion sequences.

The ideology is described here: INSERT FINAL DOI HERE

To analyze your own data, first extract SOR and sCLIP reads using the bash script reads_analysis.sh.

Then, run the python executable prepfile.py to convert to csv and add the proper headers.

> python prepfile.py

Place these output files in the "SOR Data" and "sCLIP Data" folders within the
"analyze_clusters" folder. Name these files according to the reference accession number. For
example, if analyzing data on C.diff, the files may be named "FN545816_sor.csv" and
"FN545816_sclip.csv" in each respective folder. Example data for C.diff has been included.

Edit accession_list.txt to include the accession numbers for which inversion analysis
is to be performed.

Finally, run the detection script using python:
> python detect_inversion_clusters.py

This requires Python 3.6+ and the following packages:

- Matplotlib
- BioPython
- Numpy
- Seaborn
- ReportLab

If you use these scripts in work contributing to a scientific publication, 
we ask that you cite our application. Our work is licensed generously.

If you have any questions, comments, ideas, or cool gumbo recipes, please reach us at:
Ognjen.Sekulovic@tufts.edu
jacob.bourgeois@tufts.edu

Thanks and happy hunting!
