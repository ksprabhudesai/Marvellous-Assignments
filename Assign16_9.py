def main():
    count=10
    cnt=0
    Res =""

    for i in range(1,30):
        if i%2==0 and cnt < count:
            Res = Res + str(i) + "\t"
            cnt=cnt+1

    print(Res)

if __name__ == "__main__":
    main()

    
