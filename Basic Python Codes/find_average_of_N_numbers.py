N=int(input("Enter a N number to find Average: "))
a=[]
for i in range(0,N):
    val=int(input("Enter a Values: "))
    a.append(val)
avg=sum(a)/N
print("Given input's AVg is: ",avg)