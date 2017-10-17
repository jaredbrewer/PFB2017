#!/usr/bin/env python3
import sys

dna = sys.argv[1]
codon = sys.argv[2]

if codon in dna :
	print(codon, "is present")
else :
	print(codon, "is not present")
