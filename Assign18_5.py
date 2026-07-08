import MarvellousNum

def main():
    size = 0
    Arr = list()

    print("Enter the number of elements : ") 
    size = int(input())

    print("Enter the elements : ")
    for i in range(size):
        no = int(input())
        Arr.append(no)
    
    print(Arr)

    v_prime_list = []
    sum_list=0
    for i in range(size):
        v_prime_list = list(filter(MarvellousNum.CheckPrime, Arr))
    
    print(v_prime_list)
    sum_list=MarvellousNum.Add_list(v_prime_list)
    print("Sum of prime numbers is : ",sum_list)    


if __name__ == "__main__":
    main()