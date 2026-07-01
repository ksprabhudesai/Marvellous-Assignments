def F_Even(val1):
    if val1 % 2 == 0:
        return False
    else:
        return True

def main():
    num = int(input("Enter a number: "))
    EvenList=[]
    
    for i in range(1, (num+1)):
        if F_Even(i):
            EvenList.append(i)
        

    print(f" {EvenList}")

if __name__ == "__main__":
    main()