#!/usr/bin/env python3
import sys

ran = range(int(sys.argv[1]),int(sys.argv[2]))

odds = [num for num in ran if num%2 != 0]
print(odds)