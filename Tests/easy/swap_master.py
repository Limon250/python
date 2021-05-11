"""
Problem Statement
The SwapMaster is known to be the greatest and fastest swapper of all time. You intend to bring him down and become the new SwapMaster 
of the city. Through some secret sources, you found out that The SwapMaster undertook yet another task from Dr. Symmetry. The task he 
undertook is to perform a Symmetric Swap on an array A of numbers. Perform this task before SwapMaster to become the new SwapMaster. 
A Symmetric Swap involves swapping a number in an array with its symmetric position in the array. For example, if you want to swap 
element at position 2, you will swap it with the 2nd element from the back of the array.

Input
First line contains N, denoting the number of elements in the array A. Next line contains N space-separated positive numbers.

Output
Print the array after performing the Symmetric Swap on it.

Constraints
2 ≤ N ≤ 100 
1 ≤ A[i] ≤ 1000

Sample Input
6
1 2 3 4 5 6

Sample Output

6 5 4 3 2 1
"""

import sys

N = int(input())

try:
	N = int(N)
except ValueError:
	sys.exit(0)

if 2 <= N and N <= 100:
	A = list(map(int, input().split()))
	if 1 <= len(A) and len(A) <= 1000:
		A.sort(reverse=True)
		b = " ".join(str(i) for i in A)
		print(b)
else:
	sys.exit(0)