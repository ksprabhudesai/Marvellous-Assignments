def main():
    num1 = int(input("Enter first number :"))
    num2 = int(input("Enter second number :"))

    Data_Min = lambda x,y: x if x < y else y
    res = Data_Min(num1, num2)

    print("The minimum of the two numbers is:", res)

if __name__ == "__main__":
    main()  