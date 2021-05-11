"""
Bob has a floating point number N. He wants to set the precision for 2 digits
after the decimal point for the number. He is not good at coding, hence looking 
for your help.

The first line contains T, the number of test cases. Next T line contains 
floating point number N.

Print N in a separate line after setting precision for 2 digits after 
the decimal point:

Constraints
1 <= T <= 1000 1 <= N <= 10000

Sample Input
1
713.166

Sample Output

713.17
"""

import sys

T = input()

try:
    T = int(T)
except ValueError:
    sys.exit(0)
    
if 1 <= T and T <= 1000:
    for i in range(T):
        N = input()

        try:
            N = float(N)
        except ValueError:
            sys.exit(0)

        if 1 <= N and N <= 10000:
            N = round(N, 2)
            print(N)
else:
    sys.exit(0)