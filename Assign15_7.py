
CheckLength = lambda x: (x if len(x) > 5 else None)

def main():
    n = int(input("How many elements do you want to enter? "))

    my_list = []
    for i in range(n):
        element = input(f"Enter element {i+1}: ")
        my_list.append(element)

    print("Your final list:", my_list)
    List_Even = list(filter(CheckLength, my_list))
    if not List_Even:
        print("There is no string with length greater than 5 in the list.")
    else:
        print("Strings with length greater than 5 in the list are:", List_Even)

if __name__ == "__main__":
    main()