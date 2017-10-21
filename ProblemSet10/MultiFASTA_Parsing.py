#!/usr/bin/env python3
import sys
import re

fasta = sys.argv[1]
seqs = ""
nt_comp = {}
for sequence in fasta:
    if not sequence.startswith(">"):
        seqs = sequence.rstrip().split()
        print(seqs)
        for entry in seqs:
            A_count = entry.count("A")
            print(A_count)
            T_count = entry.count("T")
            print(T_count)
            G_count = entry.count("G")
            print(G_count)
            C_count = entry.count("C")
            print(C_count)


fasta = open("Python_08.fasta", "r")
seqs = ""
genes = {}
for line in fasta:
    line = line.rstrip()
    if not line.startswith(">"):
        seqs = line.split()
        for seq in seqs:
            # A_count = seq.count("A")
            # print(A_count)
            # T_count = seq.count("T")
            # print(T_count)
            # G_count = seq.count("G")
            # print(G_count)
            # C_count = seq.count("C")
            # print(C_count)
        # print(seqs)
    if line.startswith(">"):
        headers = line.rstrip().split()
        # print(headers)

fasta = open("Python_06.fasta", "r")
seqs = ""
header = ""
seq_dict = {}
for line in fasta:
    line = line.rstrip()
    if not line.startswith(">"):
        seqs = line
        seq_dict[header] += seqs
    if line.startswith(">"):
        header = line.lstrip(">")
        seq_dict[header] = ""

nt_counts = {}
for genename, sequence in seq_dict:
    nt_counts[genename]["A"] = sequence.count("A")

counts_keys = ""
for key in seq_dict:
    nt_counts[counts_keys] = key
    for value in seq_dict:
        nt_counts[key]["A"] = value.count("A")
        nt_counts[key]["T"] = value.count("T")
        nt_counts[key]["G"] = value.count("G")
        nt_counts[key]["C"] = value.count("C")

def nuc_content(dna_dictionary):
    A_count = dna_dictionary[key].count("A")
    T_count = dna_dictionary.count("T")
    G_count = dna_dictionary.count("G")
    C_count = dna_dictionary.count("C")


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
