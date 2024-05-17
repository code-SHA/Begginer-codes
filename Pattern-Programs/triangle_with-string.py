def Triangle_String(l):
    length=len(l)
    for i in range(length):
        for j in range(i):
            print(" ",end="")
        for j in range(length-i):
            print(l[j],end=" ")
        print("\n")
l=input("Enter a String: ")
Triangle_String(l)