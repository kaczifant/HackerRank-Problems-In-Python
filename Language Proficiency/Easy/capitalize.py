# https://www.hackerrank.com/challenges/capitalize/problem

'''
You are asked to ensure that the first and last names of people begin with a capital letter 
in their passports. 
For example, 'alison heck' should be capitalised correctly as 'Alison Heck'.

Note: in a word only the first character is capitalized. 
'12abc' when capitalized remains '12abc'.
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):

    words = s.split(' ')
    for i in range(len(words)):
        words[i] = words[i].capitalize()
    
    return ' '.join(words)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
