def Odd_Star_Pattern(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end="")
        for j in range(2*i+1):
            print("*",end="")
        print("\n")
n=int(input("Enter a Row's Range: "))
Odd_Star_Pattern(n)