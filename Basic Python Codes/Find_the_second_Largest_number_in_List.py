list1=[]
num=int(input("Enter a Range You Gave me: "))
for i in range(0,num):
    elements=int(input("Enter the Element: "))
    list1.append(elements)
list1.sort()
print("Second Largest Number is",list1[-2])