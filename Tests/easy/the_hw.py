"""
Problem Statement
As the students were not focusing much on the lecture. The professor became very angry and decided to give a homework to all the students. So some of the students started trying to convince the professor not to do so. So the professor gives them a K digits and asks the students to make the largest number possible from these digits. If they able to do it, they don't need to do the homework. So you being the smartest student decided to solve the problem.

Input
The first line of input consists of single integer T denoting the number of test cases. The first line of each test case has a single integer K. The second line of each test case consists of K space separated integers denoting K digits.

Output
Print the largest number possible using these digits.

Constraints
1<=T<=100. 1<=K<=100. 0<=Digits<=9.

Sample Input
1
5
1 4 5 9 2

Sample Output

95421
"""

import sys
#import numpy as np

import sys
#import numpy as np

def main():
    T = int(input())
    K = int(input())
    try:
        T = int(T)
    except ValueError:
        sys.exit(0)

    if 1 <= T and T <= 100:
        for i in range(T):
            if 1 <= K and K <= 100:
#                    ai = np.random.randint(1, K+1, K)
                ai = list(map(int, input().split()))
#                print(ai)
                ai.sort(reverse=True)
#                ai = np.array(ai)
                if 0 <= len(ai) and len(ai) <= 9:
                    b = "".join(str(x) for x in ai)
                    print(b)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()