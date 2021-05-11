"""
You have a number of stones with known weights w1, …, wn. Write a program that will rearrange the stones into two piles such that weight 
difference between the piles is minimal.

Input
Input contains the number of stones n (1 ≤ n ≤ 20) and weights of the stones w1, …, wn (integers, 1 ≤ wi ≤ 100000) delimited by white spaces.

Output
Your program should output a number representing the minimal possible weight difference between stone piles.

Example:
Input					Output
5						3
5 8 13 27 14
"""

import sys

def main():
	n = int(input()) #number of stones
	try:
		n = int(n)
	except ValueError:
		sys.exit(0)
	k = []

	if n >= 1 and n <= 20:
		for i in range(n):
			w = int(input())
			try:
				w = int(w)
			except ValueError:
				sys.exit(0)
			if w >= 1 and w <= 100000:
				k.append(w)
			else:
				sys.exit(0)
	else:
		sys.exit(0)

	c = k[1] - k[0]
	print(c)


if __name__ == "__main__":
	main()