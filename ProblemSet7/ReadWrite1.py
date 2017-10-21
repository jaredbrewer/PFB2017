#!/usr/bin/env python3

TomPetty = open("Python_05.txt", "r")
for lyric in TomPetty:
    lyric = lyric.upper()
    print(lyric)

TomPetty = open("Python_05.txt", "r")
TomPetty_upper = open("Python_05_uc.txt", "w")
for lyric in TomPetty:
    lyric = lyric.upper()
    TomPetty_upper.write(str(lyric) + "\n")

fastas = open("Python_05.fasta.txt", "r")
seq_list = []
seqs = ""fastas = open("Python_05.fasta.txt", "r")
seq_list = []

for seq in fastas:
    if not seq.startswith(">"):
        seq = seq.rstrip("\n")
        seq = seq.split()
        seq_list.append(seq)
print(seq_list)

    seq = seq.rstrip()
    id,sequence = seq.split(">")
    seq_dict[id] = sequence


fastas = open("Python_05.fasta.txt", "r")
seqs = ""
for line in fastas:
     if not line.startswith(">"):
             line = line.rstrip()
             seqs += line
     if line.startswith(">"):
             print(seqs)
             seqs = ""
     else line.startswith(""):
         seqs = ""

print(seqs)


fastas = open("Python_05.fasta.txt", "r")
seqs = ""
for line in fastas:
     if not line.startswith(">"):
             line = line.rstrip()
             seqs += line
     if line.startswith(">"):
             print(seqs)
             seqs = ""
     else :
             seqs += "\n"

fastas = open("Python_05.fasta.txt", "r")
seqs = ""
for line in fastas:
    if not line.startswith(">"):
            line = line.rstrip()
            seqs += line
    if line.startswith(">"):
            print(seqs)
            seqs = ""

        
