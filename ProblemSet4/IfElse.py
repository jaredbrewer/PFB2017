#!/usr/bin/env python3
import sys

user_number = float(sys.argv[1])

if user_number < 0 :
	print(user_number, "is negative")
elif user_number > 50 :
	print(user_number, "is greater than 50")
elif user_number%2 == 0 :
	print(user_number, "is even")
elif user_number%3 == 0 :
	print(user_number, "is divisible by three")
else :
	print(user_number, "fulfills none of these conditions")
