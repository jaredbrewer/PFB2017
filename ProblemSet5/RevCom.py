#!/usr/bin/env python3
import sys
import math

# This will calculate the AT/GC content of a sequence and then output the reverse complement.

dna = "GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACAGAAACACTTTTCG"

print("There are", dna.count('A'), "A's in this sequence", "and there are", dna.count('T'), "T's in this sequence.")

print("There are", dna.count('G'), "G's in this sequence", "and there are", dna.count('C'), "C's in this sequence.")

AT_content = (dna.count('A') + dna.count('T'))/len(dna)
print("{:.1%}".format(AT_content))
GC_content = (dna.count('G') + dna.count('C'))/len(dna)
print("{:.1%}".format(GC_content))

rev = dna[::-1]

T2a = rev.replace("T", "a")
A2t = T2a.replace("A", "t")
G2c = A2t.replace("G", "c")
C2g = G2c.replace("C", "g")

comp = C2g.upper()

# This section will find an EcoRI site in the DNA and then output the two fragments to a list.
# We will then output relevant information properly formatted.

ecori = dna.split('GAATTC')
dna_loc = dna.find("GAATTC")
dna_len1 = len(ecori[0])
dna_len2 = len(ecori[1])

frag1_info = print("The first sequence is {} and ends at position {} and is {} nucleotides long.".format(ecori[0], dna_loc, dna_len1))
frag2_info = print("The second sequence is {} and begins at position {} and is {} nucleotides long.".format(ecori[1], dna_loc, dna_len2))

# The next step will be to sort the output of the ecori object, resort by fragment length, and then explore list copying.
