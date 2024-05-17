def pyramid(num):
    for i in range(1,num+1):
        for j in range(1,1+i):
            print("* ",end="")
        print("\n")
num=int(input("Enter a Range of a Simple Pyramid: "))
show=pyramid(num)
print(show)