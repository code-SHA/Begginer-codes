def sandclock_pattern(n):
    for i in range(n,0,-1):
        for j in range(n,i,-1):
            print(end=" ")
        for k in range(0,i):
           print("* ",end="")
        print("\n")
    for i in range(1,n):
        for j in range(0,n-i-1):
            print(end=" ")
        for k in range(0,i+1):
            print("* ",end="")
        print("\n")
n=int(input("Enter a Range to Print Sandclock: "))
sandclock_pattern(n)    