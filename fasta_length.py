#!/usr/bin/env python
# coding: utf-8


import os
import argparse

parser = argparse.ArgumentParser(description='Path to genome.fasta')
parser.add_argument('indir', type=str, help='Input file fasta')
parser.add_argument('outdir', type=str, help='Output dir for kariotype')
args = parser.parse_args()

path = args.indir

species = path.split('/')[-1].split('.')[0]
i = 0
new_lines = []
full_length = 0
concrete_length = 0

with open(path) as fasta:
    for line in fasta:
        if line[0] == '>':
            if i == 0:
                pass
            else:
                numbers = str(i) + "\t" + str(full_length) + "\t" + str(concrete_length) + "\n" 
                new_lines.append(numbers)
            i += 1
            full_length += concrete_length
            concrete_length = 0
            
        else:
            length = len(line.strip())
            concrete_length += length
    numbers = str(i) + "\t" + str(full_length) + "\t" + str(concrete_length) + "\n" 
    new_lines.append(numbers)    

path_2 = args.outdir + species + ".mmseqDB.index"

with open(path_2, 'w') as output_file:
    for line in new_lines:
        output_file.write(line)

