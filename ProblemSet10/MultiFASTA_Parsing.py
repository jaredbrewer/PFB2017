#!/usr/bin/env python3
import sys
import re

fastafile = open("Python_08.fasta", "r")
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

A = ''
T = ''
G = ''
C = ''
nt_count = {}

for gene in sequences:
    value = sequences[gene]
    A = value.count("A")
    T = value.count("T")
    G = value.count("G")
    C = value.count("C")
    nt_count[gene] = {"A": A,"T": T,"G": G,"C": C}
