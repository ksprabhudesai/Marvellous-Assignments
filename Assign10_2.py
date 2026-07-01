def main():
    num = int(input("Enter a number: "))
    result = 0

    for i in range(1, (num+1)):
        result = result + i
        
    print(f" {result}")

if __name__ == "__main__":
    main()