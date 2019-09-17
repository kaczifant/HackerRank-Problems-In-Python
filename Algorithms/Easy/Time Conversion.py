# https://www.hackerrank.com/challenges/time-conversion/problem?h_r=profile

#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    if s[-2:] == "PM":
        if s[:2] == "12":
            return s[:-2]
        else:
            return str(int(s[:2]) + 12) + s[2:8]
    else:
        if s[:2] == "12":
            return "00" + s[2:8]
        else:
            return s[:-2]




if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
