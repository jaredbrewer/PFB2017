#!/usr/bin/env python3
import sys
import statistics

# This code is HIGHLY specific to four-line FASTQ files. Variations WILL NOT WORK.
fastq = open('pfb.fastq', 'r')
seq = ''
score = ''
headers = ''
curated = {}
count = 1
for line in fastq:
    line = line.rstrip()
    if count % 4 == 1:
        headers = line
    if count % 4 == 2:
        seq = line
    if count % 4 == 0:
        score = line
    curated[headers] = [seq, score]
    count += 1
curated[headers] = [seq, score]

# The previous code successfully coerces the FASTQ into a dictionary with
# the key as the header and the value being a list of sequence and quality information.

seq_lens = {}
length = 0
std = 0
for key in curated:
    length += len(curated[key][0])/len(curated)
std = numpy.std(length)
seq_lens[key] = [length, std]

# This is the section for the quality scores that can be measured as distinct from the sequence.
seq_qcs = {}
length = 0
std = 0
score_list = []
for key in curated:
    phred = list(curated[key][1])
    scores_dict[key] += phred
    for k in scores_dict:
        for i in scores_dict[k]:
            score = ord(i) - 33
            score_list.append(score)
        score_avg = numpy.mean(score_list)
for key in curated:
    length += len(curated[key][0])/len(curated)
std = numpy.std(score_list)
seq_qcs[key] = [score_avg, std]


for key in curated:
    length += ord(curated)
    length += len(curated[key][1])/len(curated)
std = numpy.std(length)
seq_lens[key] = [length, std]



    length += len(curated[key][0])
    mean_len = statistics.mean(float(length))
    mean_len = int(count(curated[key][0])) / int(len(curated[key][0]))
    std_len = float('')

    mean = curated[key][0] / len(curated[key][0])
    mean_len[key] = mean
    length = len(curated[key][0])
    std_len[key] =