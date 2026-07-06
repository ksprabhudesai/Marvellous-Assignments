def main():
    num = int(input("Enter a number :"))
    Data_Cube = lambda x: x * x * x
    res = Data_Cube(num)

    print("The cubes of the numbers are:", res)

if __name__ == "__main__":
    main()  