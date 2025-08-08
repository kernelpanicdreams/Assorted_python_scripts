userinput: str = input("Enter the input to be repeated: ")
repeatNumber = int(input("Enter the repeat number: "))
for i in range(repeatNumber):
    print(str(i + 1) + ". " + userinput)
