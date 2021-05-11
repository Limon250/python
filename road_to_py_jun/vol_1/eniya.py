import sys

N = int(input())
A = int(input())
B = int(input())

try:
    N = int(N)
    A = int(A)
    B = int(B)
except ValueError:
    sys.exit(0)

if 1 <= N and N <= 100:
    if 1 <= A and A <= 100:
        if 1 <= B and B <= 100:
            S = N * 2 * (A + B)
            print(S)
else:
    sys.exit(0)