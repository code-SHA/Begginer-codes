def butterfly(n):
    for i in range(1,n):
        print("*"*i,end="")
        print(" "*((n-i)*2),end="")
        print("*"*i)
    for i in range(n,0,-1):
        print("*"*i,end="")
        print(" "*((n-i)*2),end="")
        print("*"*i)
n=int(input("Enter a Range for Butterfly: "))
butterfly(n)