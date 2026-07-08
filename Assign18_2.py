def main():
    result=[]
    List_Max=0

    Num1=int(input("Enter a number: "))
    for i in range(Num1):
        v_num=int(input("Enter a number to add in a List: "))

        result.append(v_num)
        if v_num > List_Max:
            List_Max = v_num

    print("The list is:",result)
    print("The maximum value in the list is:",List_Max)

if __name__=="__main__":
    main()