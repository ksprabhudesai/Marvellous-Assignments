def main():
    num1 = int(input("Enter number: "))
    v_fact=1

    for i in range(1,num1+1):
        v_fact=v_fact * (i)

    print("Factorial of ",num1," is ",v_fact)

if __name__ == "__main__":
    main()