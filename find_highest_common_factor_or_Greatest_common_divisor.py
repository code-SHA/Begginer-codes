num1=int(input("Enter a First Number: "))
num2=int(input("Enter a Second Number: "))
if num1>num2:
    smaller=num2
else:
    smaller=num1
for i in range(1,smaller+1):
    if((num1%i==0)and(num2%i==0)):
        gcd=i
print("The Given Number's HCF is",gcd)