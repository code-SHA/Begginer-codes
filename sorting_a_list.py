num=int(input("How many values you have to gave me: "))
ass=[]
for i in range(1,num+1):
    a=int(input("Enter a Number: "))
    ass.append(a) 
ass.sort()
print("Assdending order",ass)
ass.reverse()
print("Decending Order",ass)