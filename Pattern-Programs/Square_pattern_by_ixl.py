def square(n):
    for i in range(n):
        for j in range(n):
            print("* ",end=" ")
        print("\n")
n=int(input("Enter a Range For Square: "))
square(n)