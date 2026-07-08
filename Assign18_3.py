def main():
    result=[]
    

    Num1=int(input("Enter a number: "))
    List_Min = Num1+1
    for i in range(Num1):
        v_num=int(input("Enter a number to add in a List: "))

        result.append(v_num)
        if v_num < List_Min:
            List_Min = v_num

    print("The list is:",result)
    print("The minimum value in the list is:",List_Min)

if __name__=="__main__":
    main()