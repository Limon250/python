import sys

def main():
    a = input("a = ")
    b = input("b = ")
    c = input("c = ")
    
    try:
        a = int(a)
        b = int(b)
        c = int(c)
    except ValueError:
        print("Введены не целые числа или строка")
        sys.exit(0)
    
    new_a = (a, b, c)
    print(min(new_a))

if __name__ == "__main__":
    main()