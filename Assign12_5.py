def main():
    num = int(input("Enter a number: "))
    num_list = []
    if num < 0:
        print("The number is negative.")
    else:
        for i in reversed(range(1,num + 1)):
            num_list.append(i)
        print("The list of numbers is:", num_list)

if __name__ == "__main__":
    main()  