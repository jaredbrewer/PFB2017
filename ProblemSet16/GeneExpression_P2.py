#!/usr/bin/env python3

import sys, os, re

GE_dict = {}
read_counter = 0
genes_list = []

sam_file = open('bowtie2.sam', 'r')

for line in sam_file:
    line = line.rstrip().split()
    entry = line[2]
    if entry not in GE_dict:
        GE_dict[entry] = 1
    else:
        GE_dict[entry] += 1

rekey_dict = {}
for key in GE_dict:
    rekey_dict[key] = GE_dict[key.split("^")]



    if line[2] not in GE_dict:
        for key in GE_dict:
            GE_dict[key] = line[2]
        read_counter = 1
    else:
        if line[0] in GE_dict.items():
            continue
        else:
            for key in GE_dict:
                GE_dict[key] += 1

# Solution

#!/usr/bin/env python3

import sys, os, re

myDict = {}

fh = open('bowtie2.sam', 'r')
for line in fh:
    line = line.rstrip()
    fields = line.split('\t')
    read_name = fields[0]
    combo_name = fields[2]
    (gene_id, transcript_id) = combo_name.split('^')
    if gene_id not in myDict:
        myDict[gene_id] = set() # Using a set means that repeated additions are washed away - each entry is unique
    myDict[gene_id].add(read.name)

gene_ids = sorted(myDict, key = lambda x:len(myDict[x]), reverse=True)
for gene_id in gene_ids:
    mySet = myDict[gene_id]
    num_reads = len(mySet)
    print("{}\t{}". format(gene_id, num_reads))

sys.exit(0)



