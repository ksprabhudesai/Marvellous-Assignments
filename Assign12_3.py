def F_Addition(a, b):
    return a + b    

def F_Subtraction(a, b):
    return a - b

def F_Multiplication(a, b):
    return a * b    

def F_Division(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def main():
  
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    
    print(f"{num1} + {num2} = {F_Addition(num1, num2)}")    
    print(f"{num1} - {num2} = {F_Subtraction(num1, num2)}")    
    print(f"{num1} * {num2} = {F_Multiplication(num1, num2)}")
        
    result = F_Division(num1, num2)
    if result == "Error: Division by zero":
        print(result)
    else:
        print(f"{num1} / {num2} = {result}")

if __name__ == "__main__":
    main()
    