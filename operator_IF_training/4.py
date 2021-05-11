import sys

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

try:
    a = int(a)
    b = int(b)
    c = int(c)
except ValueError:
    sys.exit(0)

if a > 0 and b > 0 and c > 0:
    print(a, b, c)
elif a > 0 and b > 0 and c < 0:
    print(a, b)
elif a > 0 and b < 0 and c > 0:
    print(a, c)
elif a > 0 and b < 0 and c < 0:
    print(a)
elif a < 0 and b > 0 and c > 0:
    print(b, c)
elif a < 0 and b < 0 and c > 0:
    print(c)
elif a < 0 and b > 0 and c < 0:
    print(b)
else:
    print("No values")