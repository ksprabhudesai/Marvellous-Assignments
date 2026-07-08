def main():
    result=[]
    List_Add=0

    Num1=int(input("Enter a number: "))
    for i in range(Num1):
        v_num=int(input("Enter a number to add in a List: "))

        result.append(v_num)
        List_Add=List_Add+v_num


    print("The list is:",result)
    print("The sum of the list is:",List_Add)

if __name__=="__main__":
    main()