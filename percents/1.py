import sys

def main():
    a = input("a = ")

    try:
        a = int(a)
    except ValueError:
        sys.exit(0)
    
    if 1000 < a < 2000:
        print("skidka 5%")
        b = a/100*5
        a -= b
        print("цена со скидкой 5% = {}".format(a))
    elif 2000 < a < 5000:
        print("skidka 10%")
        b = a/100*10
        a -= b
        print("Цена со скидкой 10% = {}".format(a))
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()