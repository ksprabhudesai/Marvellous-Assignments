
v_Square = lambda x: x * x

def main():
    n = int(input("How many elements do you want to enter? "))

    my_list = []
    for i in range(n):
        element = int(input(f"Enter element {i+1}: "))
        my_list.append(element)

    print("Your final list:", my_list)
    squares = list(map(v_Square, my_list))
    print("The squares of the elements are:", squares)

if __name__ == "__main__":
    main()