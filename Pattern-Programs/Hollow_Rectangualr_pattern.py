def Hollow_Rectangle(n):
    c=n+2
    for i in range(n):
        for j in range(c):
            if i==0 or i==n-1 or j==0 or j==c-1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print("\n")
n=int(input("Enter a Rows of a Rectangle: "))
Hollow_Rectangle(n)