"""
Problem Statement
In Dcoder school, a student will pass if he/she satisfies the following criteria: 1. If he/she gets more than 70 marks in Mathematics. 2. If he/she gets more than 50 marks in Algorithms. Given the marks of Mathematics and Algorithms, print whether the student is passing or not.

Input
The first line contains an integer T denoting total number of test cases. Then in the next following T lines, each line contains two numbers which denote the marks in Mathematics and Algorithms respectively.

Output
For each test case, print "Pass" if all the conditions are satisfied else print "Fail".

Constraints
1<=T<=10. 1<=Marks<=100.

Sample Input
2
80 80
70 60

Sample Output

Pass
Fail
"""

T = int(input())

if 1 <= T and T <= 10:
    for i in range(T):
        marks = list(map(int, input().split()))
#        print(a_i)
        if len(marks) == 2:
            if 1 <= marks[i] and marks[i] <= 100:
                if marks[0] > 70 and marks[1] > 50:
                    print("Pass")
                else:
                    print("Fail")
        else:
            print("Fail")