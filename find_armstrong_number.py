n=int(input("Enter a Number: "))
temp=0
flag=n
while flag>0:
    digit=flag%10
    temp=temp+(digit**3)
    flag=flag//10
if n==temp:
    print("Given Number is Armstrong")
else:
    print("Given Number is Not Armstrong")