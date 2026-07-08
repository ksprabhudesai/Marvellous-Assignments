def CheckPrime(num1):
    v_flag=0
    
    if num1 == 0 or num1 == 1:
        print(num1," is not a prime number")
    elif num1 ==2 or num1 ==3 or num1 ==5 or num1 ==7:
        print(num1," is a prime number")
    elif num1 %2 ==0 or num1 % 3 ==0 or num1 % 5 ==0 or num1 % 7 ==0:
        print(num1," is not a prime number") 
    else:
        print(num1," is a prime number")
        
        
def main():
    num1 = int(input("Enter number: "))
    CheckPrime(num1)

if __name__ == "__main__":
    main()