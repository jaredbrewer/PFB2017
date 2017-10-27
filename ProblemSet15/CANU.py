  79: cd ProblemSet15
  80: fasta_file = open('ecoli_6X.fasta', 'r')
  81: from Bio import SeqIO
  82: reads_dict = SeqIO.to_dict(SeqIO.parse(fasta_file, "fasta"))
  83: reads_dit
  84: reads_dict
  85:
for entry in reads_dict:
    print(max(entry, key = len))
  86:
for entry in reads_dict:
    print(max(reads_dict, key = len))
  87:
for entry,seq in reads_dict:
    print(entry, seq)
  88:
for entry in reads_dict:
    for value in entry:
        type(value)
  89:
for entry in reads_dict:
    for value in entry:
        print(type(value))
  90:
for entry in reads_dict:
    for value in entry:
        print(type(value))
  91:
for entry in reads_dict:
    for value in entry:
        print(len(value))
  92:
for entry in reads_dict:
    seq = str(reads_dict[id].seq)
    print(seq)
  93:
for entry in reads_dict:
    seqs = str(reads_dict[id].seq)
    print(seqs)
  94:
for entry in reads_dict:
    seqs = str(reads_dict[entry].seq)
    print(seqs)
  95:
for entry in reads_dict:
    seqs = str(reads_dict[entry].seq)
    for line in seqs:
        print(len(line))
  96:
for entry in reads_dict:
    seqs = reads_dict[entry].seq
    for line in seqs:
        print(len(line))
  97:
for entry in reads_dict:
    seqs = reads_dict[entry].len
    for line in seqs:
        print(A)
  98: type(SeqRecord)
  99: dir(Bio.SeqRecord.SeqRecord)
 100:
for entry in reads_dict:
    seqs = []
    seqs.append(reads_dict[entry].seq)
    for line in seqs:
        print(len(line))
 101:
for entry in reads_dict:
    seqs = []
    seqs.append(reads_dict[entry].seq)
    for line in seqs:
        print(sorted(len(line)))
 102:
for entry in reads_dict:
    seqs = []
    seqs.append(reads_dict[entry].seq)
    for line in seqs:
        lens = []
        lens.append(len(line))
        print(sorted(lens))
 103:
for entry in reads_dict:
    seqs = []
    seqs.append(reads_dict[entry].seq)
    for line in seqs:
        lens = []
        lens.append(len(line))
        print(lens)
 104:
for entry in reads_dict:
    seqs = []
    seqs.append(reads_dict[entry].seq)
    for line in seqs:
        lens = []
        lens.append(int(len(line)))
        print(lens)
 105:
for entry in reads_dict:
    seqs = []
    seqs.append(reads_dict[entry].seq)
    for line in seqs:
        lens = []
        lens.append(len(line))
        lens.sort()
 106: lens = []
 107:
for entry in reads_dict:
    seqs = []
    seqs.append(reads_dict[entry].seq)
    for line in seqs:
        lens.append(len(line))
        lens.sort()
print(lens)
 108: %history -g