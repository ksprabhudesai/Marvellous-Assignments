def main():
    print("Enter a number")
    Num = int(input())
    Res =""

    for i in range(1,Num+1):
        Res = Res + "*" + "\t"

    print(Res)

if __name__ == "__main__":
    main()