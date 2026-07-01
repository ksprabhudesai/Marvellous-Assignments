def main():
    # Get the number of students
    num = int(input("Enter the number : "))
    num_list =[]

    for i in range(1,num):
        
        if num % i == 0:
            print(num /i)
            num_list.append(i)

    print("The factors of the given numbers is:", num_list)

    len_list = len(num_list)
    list_sum =0
    
    for i in range(0,len_list):
        list_sum=list_sum+num_list[i]
    

    if num == list_sum:
        print(f"The number {num} is perfect.")
    else:
        print(f"The number {num} is not perfect.")

if __name__ == "__main__":
    main()

