"""
Problem Statement
Steve is playing a quiz game with his brother John. As Steve just learned the concept of leap year, John wanted to test his knowledge. 
For that, John started to ask Steve whether a year is a leap year or not by giving him a random year. Steve is little confused and he asks 
your help to the quiz.

Input
The first line of input contains one integer T. Next T lines will have years given by John.

Output
For each test case print "Yes" if it is a leap year else "No".

Constraints
1<=T<=100. 10^3<=Year<=10^5.

Sample Input
2
2000
2017

Sample Output

Yes
No
"""

import random
import sys

def main():
    T = int(input())

    try:
        T = int(T)
    except ValueError:
        sys.exit(0)

    if 1 <= T and T <= 100:
        for i in range(T):
            T1 = int(input())
            T2 = random.randint(1000, 100000)

            try:
                T1 = int(T1)
                T2 = int(T2)
            except ValueError:
                sys.exit(0)

            if (T1 % 4 == 0) and (T1 % 100 != 0) or (T1 % 100 == 0):
                print("Yes")
            elif (T2 % 4 == 0) and (T1 % 100 != 0) or (T2 % 100 == 0):
                print("Yes")
            else:
                print("No")
    else:
        sys.exit(0)

if __name__ == "__main__":
    main()