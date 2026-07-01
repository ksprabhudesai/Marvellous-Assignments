def main():
    num_str = input("Enter the number: ")
    if len(num_str) < 0:
        print("The string is empty.")
    else:
        for i in reversed(num_str):
            num_str1 = i
            for j in range(1, len(num_str)):
                num_str2 = num_str[j]
               
    if num_str1 == num_str2:
        print("The number is a palindrome.")
        
    else:
        print("The number is not a palindrome.")
        

if __name__ == "__main__":
    main()