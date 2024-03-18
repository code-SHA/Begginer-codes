print("Print the all possible numbers divisible by given number")
a=int(input("Enter a Start range: "))
b=int(input("Enter a End range: "))
c=int(input("Enter a Divisible Number: "))
for i in range(a,b+1):
    if i%c==0:
        print(i,"Divisible by",c)