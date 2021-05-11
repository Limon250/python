import sys
import math as m

def main():
    x = input("x = ")

    try:
        x = float(x)
    except ValueError:
        print("Пошел нахуй гондон, научись читать задание, уебок")
        sys.exit(0)

    if x <= 0:
        x = -x
        print("x = {}".format(x))
    elif 0 < x < 2:
        x = m.pow(x,2)
        print("x = {}".format(x))
    elif x>= 2:
        x = 4
        print("x = {}".format(x))
    else:
        sys.exit(0)

if __name__ == "__main__":
    main()