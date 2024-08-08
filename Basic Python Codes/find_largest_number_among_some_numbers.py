n=int(input("Enter a Number of inputs you need to give: "))
l=[]
for i in range(0,n):
    a=int(input("Enter a Number:"))
    l.append(a)
sorted=l.sort()
print("Large number is: ",l[-1])

