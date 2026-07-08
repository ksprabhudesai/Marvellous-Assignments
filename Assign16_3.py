def add(Num1,Num2):
    return Num1 + Num2

def main():
    print("Enter first number")
    Num1 = int(input())
    print("Enter second number")
    Num2 = int(input())

    Result = add(Num1, Num2)
    print("Sum is:", Result)

if __name__ == "__main__":
    main()
