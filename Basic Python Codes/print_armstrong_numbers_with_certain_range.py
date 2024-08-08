first=int(input("Enter a First Number: "))
last=int(input("Enter a Last Number: "))
for i in range(first,last+1):
    order=len(str(i))
    value=0
    temp=i
    while temp>0:
        digit=temp%10
        value=value+digit**order
        temp=temp//10
    if i==value:
        print(i)