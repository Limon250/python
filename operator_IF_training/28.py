import sys

def main():
    a = input("Год = ")

    try:
        a = int(a)
    except ValueError:
        print("Exit")
        sys.exit(0)

    if a // 4:
        if a // 400:
            b = 366
            print("{} дней".format(b))
    else:
        b = 365
        print("{} дней".format(b))


if __name__ == "__main__":
    main()