def main():
    num1 = int(input("Enter number: "))
    
    v_fact_add=0

    for i in range(1,num1):
        if num1 % i ==0:
            v_fact_add=v_fact_add + i
            print(i," is a factor of ",num1)

    print("Sum of factors of ",num1," is ",v_fact_add)

if __name__ == "__main__":
    main()