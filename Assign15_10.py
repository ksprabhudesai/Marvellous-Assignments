
CheckEven = lambda x: (x if x % 2 == 0 else None)

def main():
    n = int(input("How many elements do you want to enter? "))

    my_list = []
    for i in range(n):
        element = int(input(f"Enter element {i+1}: "))
        my_list.append(element)

    print("Your final list:", my_list)
    List_Even = list(filter(CheckEven, my_list))
    list_even_cnt=len(List_Even)

    if not List_Even:
        print("There are no even numbers in the list.")
    else:
        print("The count of even numbers in the list is:", list_even_cnt)
        

if __name__ == "__main__":
    main()