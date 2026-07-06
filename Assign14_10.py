def main():
    num1 = int(input("Enter first number :"))
    num2 = int(input("Enter second number :"))
    num3 = int(input("Enter Third number :"))

    Data_Max = lambda x,y, z: x if (x > y and x > z) else y if (y > x and y > z) else z if (z > x and z > y) else None
    res = Data_Max(num1, num2, num3)

    print("The maximum of the three numbers is:", res)

if __name__ == "__main__":
    main()  