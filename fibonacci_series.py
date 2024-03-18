num=int(input("Enter a Number to Generate Fibonaci: "))
a,b=0,1
count=0
if num==1:
    print("Your fibonaci series is",a)
else:
    while count<num:
        print(a)
        l=a+b
        a=b
        b=l
        count+=1