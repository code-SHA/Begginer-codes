print("ARITHMETIC OPERATIONS")
def sum(a,b):
    c=a+b
    print(c)
def sub(a,b):
    c=a-b
    print(c)
def mul(a,b):
    c=a*b
    print(c)
def div(a,b):
    c=a/b
    print(c)
def mod(a,b):
    c=a%b
    print(c)
def exp(a,b):
    c=a**b
    print(c)
def floor(a,b):
    c=a//b
    print(c)

a=int(input("Enter a Number: "))
b=int(input("Enter a Number: "))
print("Action must be ADD,SUB,MUL,DIV,MOD,EXP,FLOOR")
A=input("Enter a Action to Perform: ")
A=A.lower()
if A=="sum" or A=="+":
    sum(a,b)
if A=="sub" or A=="-":
    sub(a,b)
if A=="mul" or A=="*":
    mul(a,b)
if A=="div" or A=="/":
    div(a,b)
if A=="mod" or A=="%":
    div(a,b)
if A=="exp" or A=="**":
    exp(a,b)
if A=="floor" or A=="//":
    floor(a,b)
