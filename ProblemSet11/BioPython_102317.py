#!/usr/bin/env python3
import sys
import Bio
from Bio import SeqIO
from Bio.Alphabet import DNAAlphabet

sprot_raw = "uniprot_sprot.fasta"
list_of_ids = []
count = 1
for record in SeqIO.parse(sprot_raw, "fasta"):
    # print("ID: {:s}".format(record.id))
    list_of_ids.append(record.id)
    count +=1
print(count)

sprot_str = str(SeqIO.parse(sprot_raw, "fasta"))

r"OS\=\w.+\s[a-z].+?\s"

for record in re.findall(r"^OS=[A-Z].+?$\s[a-z]?$", SeqIO.parse(sprot_raw, "fasta")):
    print(record)

for key, record in SeqIO.parse(sprot_raw, "fasta"):
    print(record.id)
    found = re.findall(r"^OS=[A-Z].+?$\s[a-z]?$", record.description)
    print(found)

sprot_dict = SeqIO.to_dict(SeqIO.parse("uniprot_sprot.fasta", "fasta"))
organisms = []
for key in sprot_dict:
    organisms += re.findall(r"OS=[A-Z].+?\s[a-z].+?\s", sprot_dict[key].description)
organisms.lstrip("OS=")
for organism in organisms:
    organism.strip("")
    organism_list += organism.split(" OS=")

for oism in organism_list:
