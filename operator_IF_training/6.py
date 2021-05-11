import sys

def main():
    a = input("a = ")
    b = input("b = ")
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        print("Введены не целые числа или строка")
        sys.exit(0)

    if a > b:
        print(a)
    else:
        print(b)

if __name__ == "__main__":
    main()