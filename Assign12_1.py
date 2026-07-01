def main():
    strInput=input("Enter an alphabet : ")
    
    if strInput=="a" or strInput=="e" or strInput=="i" or strInput=="o" or strInput=="u":
        print(f"{strInput} is a vowel.")
    else:
        print(f"{strInput} is a consonant.")    

if __name__ == "__main__":
    main()  
    