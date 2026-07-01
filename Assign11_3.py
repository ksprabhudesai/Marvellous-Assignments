def main():
    Num=int(input("Enter a number: "))
    NumList=[]
    NumList = list(map(int, str(Num)))
    sum=0
    
    for i in range(1, len(str(Num))+1):
        sum =sum + NumList[i-1]
        
    print(f"The sum of digits is {sum}.")


if __name__ == "__main__":
    main()  