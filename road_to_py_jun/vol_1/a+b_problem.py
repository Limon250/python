import sys

def main():
	a = int(input())
	b = int(input())

	try:
		a = int(a)
		b = int(b)
	except ValueError:
		sys.exit(0)

	c = a + b
	print(c)

main()