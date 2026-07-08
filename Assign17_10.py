def main():
    num1 = int(input("Enter number: "))
    total=0

    for i in str(num1):
        total=total + int(i)
    print("Sum of digits in given number : ", total)

if __name__ == "__main__":
    main()
