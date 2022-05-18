#!/usr/bin/env python
# coding: utf-8


import os
import random
import argparse

parser = argparse.ArgumentParser(description='Path to speciesname.mmseqDB.index')
parser.add_argument('indir', type=str, help='Input dir for mmseqDB.index')
parser.add_argument('outdir', type=str, help='Output dir for kariotype')
args = parser.parse_args()

path = args.indir
species = path.split('/')[-1][:2]
colors = ['black','blue','green','red']
list_lengths = []

with open(path) as lengths:
    for line in lengths:
        length = line.split('\t')[2].strip()
        list_lengths.append(int(length))
new_lines = []
list_lengths = sorted(list_lengths, reverse=True)
i = 1
for number in list_lengths:
    new_line = 'chr - ' + species + str(i) + " seq" + str(i) + ' 0 ' + str(number) + " " + random.choice(colors) + '\n'
    new_lines.append(new_line)
    i += 1
with open(args.outdir + species + '_kariotype', 'w') as output_file:
    for line in new_lines:
        output_file.write(line)
    
    
