def Diamond(n):
    for i in range(n):
        for j in range(n):
            if i+j==2 or j-i==2 or i-j==2 or i+j==6:
                print("*",end=" ")
            else:
                print(end=" ")
        print("\n")
print("You have Enter Range must be 5")
n=int(input("Enter a Range for a Diamond: "))
Diamond(n)