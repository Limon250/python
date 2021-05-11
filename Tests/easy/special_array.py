"""
Problem Statement
Natural numbers are the set of positive integers, which ranges from 1 to infinity excluding fractional part. Natural numbers are whole numbers excluding zero. Zero is the only whole number which is not a natural number. An array is special if all the elements are natural numbers. Find whether the given array is special or not.

Input
The first line of input contains a single integer N denoting the array size. The second line of input contains N-space separated integers denoting the array.

Output
Print "Yes" if the array is special else print "No".

Constraints
1<=N<=100. 0<=Arrays elements<=100.

Sample Input
4
0 1 2 3

Sample Output

No
"""

import sys

def main():
    N = int(input())

    try:
        N = int(N)
    except ValueError:
        sys.exit(0)

    if 1 <= N and N <= 100:
        a = list(map(int, input().split()))
#        print(a)
        
        if 0 in a:
            print("No")
        else:
            print("Yes")
    else:
        main()

if __name__ == "__main__":
    main()