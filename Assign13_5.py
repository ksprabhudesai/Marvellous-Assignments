def main():
    num_marks = int(input("Enter the marks: "))
    if num_marks < 0:
        print("The marks are negative.")
    else:
        if num_marks >= 75:
            print("Grade: Distinction")
        elif num_marks >= 60:
            print("Grade: First Class")
        elif num_marks >= 50:
            print("Grade: Second class")
        elif num_marks <= 50:
            print("Grade: Failed")
        
if __name__ == "__main__":
    main()
