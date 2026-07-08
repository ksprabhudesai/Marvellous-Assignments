def add(num1,num2):
    return num1 + num2

def sub(num1,num2):
    return num1 - num2

def mult(num1,num2):
    return num1 * num2

def div(num1,num2):
    if num2 == 0:
        return "Error: Division by zero"
    return num1 / num2

def main():
    
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print("Addition : ", add(num1,num2))
    print("Subtraction : ", sub(num1,num2))
    print("Multiplication : ", mult(num1,num2))
    print("Division : ", div(num1,num2))

if __name__ == "__main__":
    main()