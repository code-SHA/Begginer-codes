def Half_triangle(n):
    for i in range(n):
        for j in range(i,n):
            print(" ",end=" ")
        for j in range(i+1):
            print("*",end=" ")
        print("\n")
    for i in range(n-1):
        for j in range(i+2):
            print(" ",end=" ")
        for j in range(i,n-1):
            print("*",end=" ")
        print("\n")
n=int(input("Enter The Triangle's Range: "))
Half_triangle(n)