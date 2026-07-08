def main():
    result=[]
    v_freq=0

    Num1=int(input("Enter number of elements in the list: "))
    
    for i in range(Num1):
        v_num=int(input("Enter a number to add in a List: "))

        result.append(v_num)
    
    Num2=int(input("Enter element to be searched: "))

    for i in range(Num1):
        if result[i] == Num2:
            v_freq += 1

    print("The list is:",result)
    print("The element", Num2, "appears", v_freq, "times in the list")

if __name__=="__main__":
    main()