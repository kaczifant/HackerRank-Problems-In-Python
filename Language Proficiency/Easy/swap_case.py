# https://www.hackerrank.com/challenges/swap-case/problem

'''
You are given a string and your task is to swap cases. 
In other words, convert all lowercase letters to uppercase letters and vice versa.
'''

# Complete the function below

def swap_case(s):
    
    li = []

    for c in s:
        if c.islower():
            li.append(c.upper())
        elif c.isupper():
            li.append(c.lower())
        else:
            li.append(c)

    return ''.join(li)
	
	# or alternatively just:  return s.swapcase()


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)