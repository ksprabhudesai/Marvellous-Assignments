
Check3_5 = lambda x: (x if (x % 3 == 0 and x % 5 == 0) else None)

def main():
    n = int(input("How many elements do you want to enter? "))

    my_list = []
    for i in range(n):
        element = int(input(f"Enter element {i+1}: "))
        my_list.append(element)

    print("Your final list:", my_list)
    List_3_5 = list(filter(Check3_5, my_list))
    if not List_3_5:
        print("There are no numbers divisible by both 3 and 5 in the list.")
    else:
        print("The numbers divisible by both 3 and 5 in the list are:", List_3_5)

if __name__ == "__main__":
    main()