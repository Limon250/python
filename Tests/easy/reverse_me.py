"""
Problem Statement
You are given an integer, reverse it.

Input
Input contains an integer n.

Output
Print reverse of integer.

Constraints
1<=n<=10000

Sample Input
9956

Sample Output

6599
"""

n = int(input())
m = 0
if 1 <= n and n <= 10000:
    while n>0:
        m = m*10 + n%10
        n = n//10
    print(m)