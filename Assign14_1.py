def main():
    num = int(input("Enter a number :"))
    Data_Square = lambda x: x * x
    res = Data_Square(num)

    print("The squares of the numbers are:", res)

if __name__ == "__main__":
    main()  