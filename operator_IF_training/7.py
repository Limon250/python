import sys

def main():
    a = input("a = ")
    b = input("b = ")

    try:
        a = float(a)
        b = float(b)
    except ValueError:
        print("Введены не вещественные числа или строка!")
        sys.exit(0)

    if a > b:
        buf = a
        a = b

        print("b = {}, a = {}".format(buf,a))
    else:
        print("a = {}, b = {}".format(a,b))

if __name__ == "__main__":
    main()