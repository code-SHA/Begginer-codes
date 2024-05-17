def inverted_hollow_triangle(n):
    for i in range(n):
        for j in range(n):
            if i==0 or j==n-1 or i==j:
                print("* ",end="")
            else:
                print(" ",end=" ")
        print("\n")
n=int(input("Enter the Range of Hollow Triangle: "))
inverted_hollow_triangle(n)