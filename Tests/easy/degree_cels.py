"""
Problem Statement
Tom is a scientist. He uses huge machines for complex calculations. There is a problem, the machines takes input as Fahrenheit and Tom has the 
temperatures in Degree Celsius. As he is busy with his work, he asks your help to convert Degree Celsius to Fahrenheit.

Input
The first and only line of the input consists of a single integer T denoting temperature in Degree Celsius.

Output
Print an integer denoting temperature in Fahrenheit.

Constraints
0<=T<=1000

Sample Input
100

Sample Output

212
"""

import sys

def main():
    T = int(input())

    try:
        T = int(T)
    except ValueError:
        sys.exit(0)

    if 0 <= T and T <= 1000:
        print(int(T * 9/5 + 32))
    else:
        main()

if __name__ == "__main__":
    main()