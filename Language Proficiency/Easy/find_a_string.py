# https://www.hackerrank.com/challenges/find-a-string/problem

'''
You have to print the number of times that the substring occurs in the given string. 
String traversal will take place from left to right, not from right to left.

NOTE: String letters are case-sensitive.

For example: 
	string: 'ABCDCDC'
	substring: 'CDC'
	occurrence: 2
'''

# Complete the function below
def count_substring(string, sub_string):

    count = 0
    len_substring = len(sub_string)
    
    for i in range(len(string)-len_substring+1):
        if string[i:i+len_substring] == sub_string:
            count += 1
    
    return count
    

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)