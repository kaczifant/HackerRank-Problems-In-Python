# https://www.hackerrank.com/challenges/text-wrap/problem

'''
You are given a string S and width w.
Your task is to wrap the string into a paragraph of width w.
'''

import textwrap

# Complete the function below
def wrap(string, max_width):

    wrapped_text = textwrap.fill(string, width=max_width)
    
    return wrapped_text

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)