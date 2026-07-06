def main():
    num = int(input("Enter a number :"))
    

    Data_Min = lambda x:True if x % 2 == 0 else False
    res = Data_Min(num)

    if res:
        print("The number is even")
    else:
        print("The number is odd")

if __name__ == "__main__":
    main()  