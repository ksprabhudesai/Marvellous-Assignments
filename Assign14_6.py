def main():
    num = int(input("Enter a number :"))
    

    Data_Min = lambda x:False if x % 2 == 0 else True
    res = Data_Min(num)

    if res:
        print("The number is odd")
    else:
        print("The number is even")

if __name__ == "__main__":
    main()  