def ChkGreater(Val1, Val2):
    if Val1 > Val2:
        return True
    else:
        return False

def main():
    Num1 = int(input("Enter first number: "))
    Num2 = int(input("Enter second number: "))
    
    if ChkGreater(Num1, Num2):
        print(f"{Num1} is greater than {Num2}.")
    else:
        print(f"{Num2} is greater than or equal to {Num1}.")

if __name__ == "__main__":
    main()  
    