# https://www.hackerrank.com/challenges/python-string-split-and-join/problem

'''
You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.
'''

# Complete the function below

def split_and_join(line):
    
    return '-'.join(line.split())

if __name__ == '__main__':
    line = raw_input()
    result = split_and_join(line)
    print result