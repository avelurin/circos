#!/usr/bin/env python
# coding: utf-8


import os
import argparse

parser = argparse.ArgumentParser(description='Tool to add band in kariotype circos file')
parser.add_argument('indir', type=str, help='Kariotype file for adding')
parser.add_argument('chr', type=str, help='Name of chr in kariotype')
parser.add_argument('band_begining', type=str, help='Start posithion of band')
parser.add_argument('band_finish', type=str, help='Stop position of band')
args = parser.parse_args()



#imput kariotype file and new band[contig, star, stop]
    # band = ['ba1','50', '70']                     two stings 
    # path = '/home/aurin/projects/ba_kariotype'     to chek problems

band = [args.chr, args.band_begining, args.band_finish]
path = args.indir

#transfer input fike to list of lines
lines_list = []
with open(path) as karyotype:
    for line in karyotype:
        lines_list.append(line)

#add backgrunds bands if it nessery
if lines_list[-1].find('band') == -1:
    bands = []
    for line in lines_list:
        string = []
        string.append('band')
        col_2 = line.split(' ')[2]
        string.append(col_2)
        string.append('back' + '2' + col_2)
        string.append('background' + col_2[2:])
        string.append('0')
        string.append(line.split(' ')[5])
        string.append('white\n')
        string = " ".join(string)
        bands.append(string)
    lines_list = lines_list + bands    
        
#create new bands for input contig
old_bands = []
for line in lines_list:
    if line.split(' ')[1] == band[0]:
        old_bands.append(line)      
        
        
new_bands = []
for string in old_bands:
    old_band_start = int(string.split(' ')[4])
    old_band_stop = int(string.split(' ')[5])
    if old_band_stop < int(band[1]) or old_band_start > int(band[2]):
        new_bands.append(string)
    else:
        befor_string = []
        befor_string.append(string.split(' ')[0])
        befor_string.append(string.split(' ')[1])
        befor_string.append(string.split(' ')[2] + 'b')
        befor_string.append('befband')
        befor_string.append(string.split(' ')[4])
        befor_string.append(str(int(band[1]) - 1))
        befor_string.append(string.split(' ')[6])                   
        new_string = " ".join(befor_string)
        new_bands.append(new_string)
    
        band_string = []
        band_string.append(string.split(' ')[0])
        band_string.append(string.split(' ')[1])
        band_string.append(string.split(' ')[2] + 'm')
        band_string.append('band')
        band_string.append(band[1])
        band_string.append(band[2])
        band_string.append('black\n')
        new_string_1 = " ".join(band_string)
        new_bands.append(new_string_1)
        
        after_string = []
        after_string.append(string.split(' ')[0])
        after_string.append(string.split(' ')[1])
        after_string.append(string.split(' ')[2] + 'a')
        after_string.append('aftband')
        after_string.append(str(int(band[2]) + 1))
        after_string.append(string.split(' ')[5])
        after_string.append(string.split(' ')[6])
        new_string_2 = " ".join(after_string)
        new_bands.append(new_string_2)

        
#remowe dubled and incorrect strings in new bands
str_to_add = []
for line in new_bands:
    line_start = int(line.split()[4])
    line_stop = int(line.split()[5])
    if len(str_to_add) == 0:
        str_to_add.append(line)
        last_stop = line_stop
    elif line_start <= line_stop and line_start > last_stop:
        str_to_add.append(line)
        last_stop = line_stop


#replace old bands with new bands
changed_str = lines_list.index(old_bands[0])
for n in old_bands:
    removed = lines_list.pop(changed_str)
n2insert = 0
for line in str_to_add:
    lines_list.insert(changed_str + n2insert, line)
    n2insert += 1


with open(path, 'w') as new_karyo:
    for line in lines_list:
        new_karyo.write(line)
      





