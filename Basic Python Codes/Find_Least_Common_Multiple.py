a=int(input("Enter a First Number: "))
b=int(input("Enter a Second Number: "))
if a>b:
    greater=a
else:
    greater=b
while(True):
    if((greater%a==0)and(greater%b==0)):
        lcm=greater
        break
    greater=greater+1
print("Given Number's LCM is",lcm)    