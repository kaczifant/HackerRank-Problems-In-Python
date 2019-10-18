# https://www.hackerrank.com/challenges/nested-list/problem

'''
Given the names and grades for each student in a Physics class of N students,
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the same grade,
order their names alphabetically and print each name on a new line.

There will always be one or more students having the second lowest grade.
''' 

if __name__ == '__main__':

    students = []
    scores = set()

    for _ in range(int(input())):
        name = input()
        score = float(input())

        students = students + [[name, score]]
        scores.add(score)

    sorted_scores = sorted(scores)
    s_lowest = sorted_scores[1]
    s_lowest_names = []
    
    for student in students:
        if student[1] == s_lowest:
            s_lowest_names.append(student[0])
            
    s_lowest_names.sort()
    
    for name in s_lowest_names:
        print(name)
