n=int(input("Enter a Number: "))
if n<0:
    print("Enter a valid number..!")
else:
    temp=0
    while n>0:
        temp=temp+n
        n=n-1
print("The Sum of Natural Number is: ",temp)
