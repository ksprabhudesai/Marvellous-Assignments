def DivisionCondition(val1):
    if val1 % 3 == 0:
        if val1 % 5 == 0:
            return 1
        else:
            return 3
    else:
        if val1 % 5 == 0:
            return 5
        else:
            return 0
    

def main():
    num = int(input("Enter a number: "))
    
    if DivisionCondition(num) == 1:
        print(f"{num} is divisible by both 3 and 5.")
    elif DivisionCondition(num) == 3:
        print(f"{num} is divisible by 3 but not by 5.")
    elif DivisionCondition(num) == 5:
        print(f"{num} is divisible by 5 but not by 3.")
    else:   
        print(f"{num} is not divisible by both 3 and 5.")

if __name__ == "__main__":
    main()