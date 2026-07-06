from functools import reduce


def CheckMax(No1,No2):
    return No1 if No1 > No2 else No2


def main():
    n = int(input("How many elements do you want to enter? "))

    my_list = []
    for i in range(n):
        element = int(input(f"Enter element {i+1}: "))
        my_list.append(element)

    print("Your final list:", my_list)

    Rdata = reduce(CheckMax,my_list)
    print("Maximum element:", Rdata)

if __name__ == "__main__":
    main()
    