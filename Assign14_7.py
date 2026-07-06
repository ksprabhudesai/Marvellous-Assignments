def main():
    num = int(input("Enter a number :"))
    

    Data_Min = lambda x:True if x % 5 == 0 else False
    res = Data_Min(num)

    if res:
        print("The number is divisible by 5")
    else:
        print("The number is not divisible by 5")

if __name__ == "__main__":
    main()  