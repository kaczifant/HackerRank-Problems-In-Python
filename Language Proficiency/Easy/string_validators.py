# https://www.hackerrank.com/challenges/string-validators/problem

'''
You are given a string S.
Your task is to find out if the string S contains: 
	- alphanumeric characters
	- alphabetical characters
	- digits
	- lowercase
	- uppercase characters
'''


if __name__ == '__main__':
    s = input()

	# Enter your code below
	
    checks = [False] * 5
    
    for c in s:
        checks[0] = checks[0] or c.isalnum()
        checks[1] = checks[1] or c.isalpha()
        checks[2] = checks[2] or c.isdigit()
        checks[3] = checks[3] or c.islower()
        checks[4] = checks[4] or c.isupper()
    
    for check in checks:
        print(check)