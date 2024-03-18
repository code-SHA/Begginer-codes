num=int(input("Enter a Number to  find Factors: "))
val=1
print("The given Number's Factors shown below")
while(val<=num):
    if(num%val==0):
        print(val)
    val=val+1