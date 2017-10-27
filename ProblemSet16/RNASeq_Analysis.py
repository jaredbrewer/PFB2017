#!/usr/bin/env python3
import sys

kmer_length = int(sys.argv[1])
filename = sys.argv[2] # reads.fq from GitHub website
num_top_kmers = int(sys.argv[3])

count = 1
kmer_dict = {}
seq_list = []

for line in filename:
    if count % 4 == 2:
        sequence = line
        for nuc in sequence:
            if len(sequence) >= 8:
                seq_list.append(''.join(sequence[0:7]))
                if seq_list[0] in kmer_dict:
                    kmer_dict[seq_list[0]] += 1
                    seq_list.remove([0])
                else:
                    kmer_dict[seq_list[0]] = 1
    count += 1

def count_kmers(kmer_dict, sequence):
    # iterate through all the kmers
    for i in range(0, len(sequence)-kmer_len+1)



#### Brian's Solution ####

#!/usr/bin/env python3

# kmer_length fastq_filename num_top_report
usage = '\n\n\tusage: () kmer_length fastq_filename num_top_report\n\n\n'.format(sys.argv[0])

import sys, os

kmer_length = int(sys.argv[1])
fastq_filename = sys.argv[2]
num_top_kmers = int(sys.argv[3])

if len(sys.argv) < 4:
    sys.stderr.write(usage)
    sys.exit(1)

## Let's do it to it:

def count_kmers(kmer_dict, sequence, kmer_length):
    for i in range(0, len(sequence) - kmer_length + 1):
        kmer = sequence[i:i + kmer_length]
        if kmer in kmer_dict:
            kmer_dict[kmer] += 1
        else:
            kmer_dict[kmer] = 1
        # look up collections.defaultdict
    return

count = 1
kmer_dict = {}

fh = open('reads.fq', 'r')
for line in fh:
    count += 1
    line = line.rstrip()
    if count % 4 == 2:
        sequence = line
        count_kmers(kmer_dict, sequence, kmer_length)

# Sort the kmers
sorted_kmers = sorted(kmer_dict, key = lambda x: kmer_dict[x], reverse = True)
sorted_kmers = sorted_kmers[0:num_top_kmers]

# This is unsorted - sad, but interesting:
for (key, value) in kmer_dict.items():
    print("{}\t{}".format(kmer, count))

for kmer in sorted_kmers:
    count = kmer_dict[kmer]
    print("{}\t{}".format(kmer, count))

sys.exit(0)