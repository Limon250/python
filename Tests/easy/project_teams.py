"""
Problem Statement
There are N students in a class and Teacher want to divide these students into some groups . Teacher told  that groups consisting of 
two or less students not allowed , so Teacher want to have as many groups consisting of three or more 
students as possible. Divide the students so that the number of groups consisting of three or more students is maximized.

Input
Single integer N

Output
Maximum number of groups can be formed

Constraints
1<=N<100000

Sample Input
6

Sample Output

2
"""

import sys

def main():
    N = int(input())

    try:
        N = int(N)
    except ValueError:
        sys.exit(0)

    if 0 <= N and N < 100000:
        if N % 2 == 0:
            print(2)
        elif N % 3 == 0:
            print(3)
        elif N % 4 == 0:
            print(4)
        elif N % 5 == 0:
            print(5)
        elif N % 6 == 0:
            print(6)
        elif N % 7 == 0:
            print(7)
        elif N % 8 == 0:
            print(8)
        elif N % 9 == 0:
            print(9)
        elif N % 10 == 0:
            print(10)

if __name__ == "__main__":
    main()