def ChkPrime(val1):
    
    if val1 < 1:
        return False
    elif val1 == 2 or val1 == 3  or val1  == 5 or val1  == 7:
        return True
    elif val1 > 7:
        if val1 % 2 == 0 or val1 % 3 == 0 or val1 % 5 == 0 or val1 % 7 == 0:
            return False
        else:
            return True
    

def main():
    num = int(input("Enter a number: "))
    if ChkPrime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")

if __name__ == "__main__":
    main()
