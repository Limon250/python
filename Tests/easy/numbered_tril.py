"""
Problem Statement
You need to print this pattern upto N. For N = 4, 1 1 2 1 2 3 1 2 3 4

Input
A single positive integer N.

Output
Numbered Triangle upto N. Do not leave trailing whitespaces at the end of each line.

Constraints
1 ≤ N ≤ 9

Sample Input
3

Sample Output

1
1 2
1 2 3
"""

import sys

N = int(input())
a = list()

try:
    N = int(N)
except ValueError:
    sys.exit(0)

if 1 <= N and N <= 9:
    i = 0
    for i in range(N):
        a.append(i+1)
#        i += 1
        b = " ".join(str(x) for x in a)
        print(b)
else:
    sys.exit(0)