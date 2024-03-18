line=str(input("Enter a String: "))
if line.islower():
    print("Your String is LowerCase")
elif line.istitle():
    print("Your String is TitleCase")
else:
    print("Yout String is UpperCase")