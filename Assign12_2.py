def main():
    Num=int(input("Enter a number: "))
    FactList=[]

    for i in range(1, Num+1):
        if Num % i == 0:
            FactList.append(i)

    print(f"The factors of {Num} are: {FactList}")

if __name__ == "__main__":
    main()

