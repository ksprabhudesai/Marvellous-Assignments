def main():
    num1 = int(input("Enter first number :"))
    num2 = int(input("Enter second number :"))
    

    Data_Max = lambda x,y: x if x > y else y
    res = Data_Max(num1, num2)

    print("The maximum of the two numbers is:", res)

if __name__ == "__main__":
    main()  