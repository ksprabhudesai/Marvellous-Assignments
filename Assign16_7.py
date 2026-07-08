def Check5(num):
    if num % 5 == 0:
        return True
    else:
        return False
    
def main():
    print("Enter Number")
    Value = int(input())

    Ret = Check5(Value)
    print(Ret)

if __name__ == "__main__":
    main()