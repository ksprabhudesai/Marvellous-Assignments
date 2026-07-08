def main():
    num1 = int(input("Enter number: "))
    v_design=""

    for i in range(num1):
        for j in range(num1):
            v_design = v_design + "*"

        print(v_design)
        v_design=""

if __name__ == "__main__":
    main()