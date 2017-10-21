#!/usr/bin/env python3
import sys

fastafile = open("Python_05.fasta.txt", "r")
seq = ''
header = ''
sequences = {}
for line in fastafile:
    line = line.strip()
    if line.startswith(">"):
        if seq != '':
            sequences[header] = seq
            seq = ''
        header = line
    else:
        seq += line
sequences[header] = seq

for seq in sorted(sequences.keys()):
    print(seq)
    