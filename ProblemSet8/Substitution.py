#!/usr/bin/env python3

import re

# Question 1
ShelSilverstein = open("Python_06_nobody.txt", "r")
for item in re.finditer(r"Nobody", ShelSilverstein.read()):
    print("Nobody begins at", item.start(), "and Nobody ends at", item.end())
# Question 2
ShelSilverstein = open("Python_06_nobody.txt", "r")
output = open("Jared.txt", "w")
output.write(re.sub(r"Nobody", "Jared", ShelSilverstein.read()))

histones = open("Python_06.fasta.txt", "r")
for header in re.finditer(r"^>.+$", histones.read(), re.M):
    print(header)

# Question #3

histones = open("Python_06.fasta.txt", "r")
for header in re.finditer(r"^>.+$", histones.read(), re.M):
    print(header)

histones = open("Python_06.fasta.txt", "r")
for seq in fastas:
    if seq.startswith(">"):
        for header in re.finditer(r"^>.+$", histones.read(), re.M):
    print(header)

# Question #4
histones = open("Python_06.fasta.txt", "r")
hist = histones.read()
gene_name = re.findall(r"^>.+?\|", hist)
desc = re.findall(r"\|.+?$", hist)

for (gene, desc) in re.findall(r"(^>.+?\|)(\|.+$)", hist):
    print(gene)
    print(desc)

for line in histones:
    if line.startswith(">"):
        for gene in re.findall(r"^\>.+?\|", line)        
        for desc in re.findall(r"\|.+?$", line)
    print(gene, desc)

    gene_name = gene_desc.group(1)
    desc = gene_desc.group(2)
print(gene_name, desc)
