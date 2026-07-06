def main():
    num1 = int(input("Enter first number :"))
    num2 = int(input("Enter second number :"))

    

    Data_Min = lambda x,y : x+y
    res = Data_Min(num1,num2)

    
    print("The sum of the two numbers is:", res)

if __name__ == "__main__":
    main()  