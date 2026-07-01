def main():
    num = int(input("Enter a number: "))
    if num < 0:
        print("The number is negative.")
    else:
        #num_bin = bin(num)[2:]  # Convert to binary and remove the '0b' prefix
        num_bin = format(num, 'b')  # Convert to binary using format function
        print("The binary representation of the number is:", num_bin)

if __name__ == "__main__":
    main()
        