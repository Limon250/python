"""
Input
The input stream contains a set of integer numbers Ai (0 ≤ Ai ≤ 1018).
The numbers are separated by any number of spaces and line breaks. 
A size of the input stream does not exceed 256 KB.

Output
For each number Ai from the last one till the first one you should output
its square root. Each square root should be printed in a separate line with 
at least four digits after decimal point.
"""

import sys
import math as m

def main():
	Ai = int(input()) #кол-во чисел
#	N = []
	try:
		Ai = int(input())
	except ValueError:
		sys.exit(0)
	
	if 0 <= Ai and m.pow(10, 18) >= Ai:
		for i in range(Ai):
#			N.append(int(input()))
			N = int(input()) #ввод чисел

			try:
				N = int(N)
			except ValueError:
				sys.exit(0)

			for i in range(N, N + 1):	
				print(round(m.sqrt(N),4))
	else:
		sys.exit(0)


if __name__ == "__main__":
	main()