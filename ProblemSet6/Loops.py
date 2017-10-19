#!/usr/bin/env python3

count = 0
while count < 101 :
    print("count:", count)
    count += 1
print("All finished.")

num = 1000
factorial = 1

while num > 0 :
    factorial = factorial * num
    num -= 1
print(factorial)

random_nums = [101,2,15,22,95,33,2,27,72,15,52]
random_iter = iter(random_nums)

even_nums = [print(num) for num in random_nums if num%2 == 0]
odd_nums = [print(num) for num in random_nums if num%2 != 0]

random_nums.sort()
sorted_iter = iter(random_nums.sort())

odd_nums = [num for num in random_nums if num%2 != 0]
sum(odd_nums)
even_nums = [num for num in random_nums if num%2 == 0]
sum(even_nums)

# Stopped at question #6

ran = range(1:101)

for num in ran:
    print(num)

ran = range(sys.argv[1]:sys.argv[2])

for num in ran: 
    print(num)

#!/usr/bin/env python3                                                          
import sys

ran = range(int(sys.argv[1]),int(sys.argv[2]))

for num in ran:
    print(num)

#!/usr/bin/env python3
import sys

ran = range(int(sys.argv[1]), int(sys.argv[2]))

odds = [num for num in ran if num%2 != 0]
print(odds)

seqs = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

for seq in seqs: 
    print(seq)

seq_tuple = ([seq for seq in seqs], [len(seq) for seq in seqs])

for seq in seqs:
    print(len(seq), seq)

