# https://www.hackerrank.com/challenges/python-string-formatting/problem

'''
Given an integer, n, print the following values for each integer i from 1 to n:
	- Decimal
	- Octal
	- Hexadecimal (capitalized)
	- Binary
	
The four values must be printed on a single line in the order specified above for each i from 1 to n. 
Each value should be space-padded to match the width of the binary value of n.
'''

# Complete the function below
def print_formatted(number):
    
    bin_width = len(bin(number))-2

    for x in range(1, number+1):
        dec = str(x)
        octal = oct(x)[2:]
        hexdec = hex(x)[2:].upper()
        binary = bin(x)[2:]
        
        print((dec.rjust(bin_width, ' ')), end=' ')
        print((octal.rjust(bin_width, ' ')), end=' ')
        print((hexdec.rjust(bin_width, ' ')), end=' ')
        print((binary.rjust(bin_width, ' ')), end=' ')
        
        print()

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)