"""
Problem Statement
You are given an integer array and you have to find the sum of the elements of the array and find the remainder when the sum is divided by the largest number of the array.

Input
First line contains N, the number of elements. Next line contains N space separated integers (elements of the array).

Output
Print the remainder when sum is divided by the maximum element.

Constraints
1 ≤ n ≤ 100 0 ≤ A[i] ≤ 1000

Sample Input
5
1 2 3 4 5

Sample Output

0
"""

import sys
#import numpy as np

def main():
    N = int(input())

    try:
        N = int(N)
    except ValueError:
        sys.exit(0)

    if N >= 1 and N <= 100:
        a = list(map(int, input().split()))
#        print(a)
        if len(a) >= 0 and len(a) <= 1000:
            total = sum(a) #sum of array
#           print(total) #print sum of array
            b = total % max(a) #remainder
            print(b) #print the remainder
    else:
        main()

    

if __name__ == "__main__":
    main()