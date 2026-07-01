def main():
    num = int(input("Enter a number: "))
    Tablelist=[]

    for i in range(1, 11):
        result = num * i
        Tablelist.append(result)

    
    print(f" {Tablelist}")
    
if __name__ == "__main__":
    main()