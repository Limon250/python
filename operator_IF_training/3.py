import sys

a = int(input("a = "))

try:
    a = int(a)
except ValueError:
    sys.exit(0)

if a > 0:
    a += 1
    print(a)
elif a < 0:
    a -= 2
    print(a)
else:
    a = 10
    print(a)