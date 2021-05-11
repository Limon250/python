import sys

def main():
    a = input("a = ")
    b = input("b = ")

    try:
        a = int(a)
        b = int(b)
    except ValueError:
        print("Введены неверные числа или строка")
        sys.exit(0)
    
    if a != b:
        c = a + b
        print("{}".format(c))
    elif a == b:
        a = 0
        b = 0
        print("a = {}, b = {}".format(a, b))


if __name__ == "__main__":
    main()