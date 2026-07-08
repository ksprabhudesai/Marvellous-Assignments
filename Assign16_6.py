def checknum(num):
    
    if num > 0:
        print("The number is positive.")
    elif num < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")

def main():
    print("Enter a number:")
    value = int(input())
    checknum(value) 

if __name__ == "__main__":
    main()