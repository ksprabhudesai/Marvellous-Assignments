def main():
    strInput=input("Enter a number: ")
    NumList=[]
    NumList = list(map(int, str(strInput)))
    sum=""

    for i in reversed(range( 1,len(strInput)+1)):
        sum =sum + str(NumList[i-1])
        
    print(f"The reverse of the given number is {sum}.")


if __name__ == "__main__":
    main()  