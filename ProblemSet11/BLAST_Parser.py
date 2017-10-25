#!/usr/bin/env python3
from glob import glob

direc = glob('./*.txt')

for file in direc:
    files = open(file, "r")
    for line in files:
        line_strip = line.strip()
        if line_strip.startswith('#'):
            continue
        else:
            BLAST_dict[file] = line_strip.split('\t')

for key,value in BLAST_dict.items():
    print(key," - ", "\n Percent ID:", value[2], "\n Alignment Length:", value[3], "\n E-Value:", value[10], "\n Query Length:", int(value[7])-int(value[6]))
