def CheckNum(Num):
    if Num % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")

def main():
    print("Enter Number")
    Value = int(input())

    CheckNum(Value)

if __name__ == "__main__":
    main()
    