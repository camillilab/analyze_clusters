#!/bin/bash

#### command lines used for same-orientation-reads (SOR) and 5-prime soft clipped reads (sCLIP) extraction from .fastq files following bwa alignement ####

# Alignment of paired-end .fastq files on the reference genome using bwa. #
# Final alignment is further processed based on the mapping quality (MAPQ), based on the premise #
# that read mapping to multiple locations with the same quality are given a score of "0". #

bwa index -p INDEX reference.fasta
bwa aln INDEX file_1.fastq > file_1.sai
bwa aln INDEX file_2.fastq > file_2.sai
bwa sampe INDEX file_1.sai file_2.sai file_1.fastq file_2.fastq | samtools view -q 1 > aln.sam

# Extraction of same-orientation-reads (SOR) #

awk '$2 ~ /113|177|65|129/ {print $2, $4, $6, $9}' aln.sam > SOR.txt

# Extraction of 5-prime soft clipped reads (SOR) #

awk '($2 ~ /147|83/ && $6 ~ /^..?S/) || ($2 ~ /99|163/ && $6 ~ /S$/) {next;} $6 ~ /^..?S/ {print $2, $4, $6, $9 }' aln.sam > sCLIP.txt

# End