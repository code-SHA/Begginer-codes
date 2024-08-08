line=input("Enter the Word: ")
line2=' '
for i in line:
    if(i>='a' and i<='z'):
        line2=line2+chr((ord(i)-32))
    elif(i>='A' and i<='Z'):
        line2=line2+chr((ord(i)+32))
    else:
        line2=line2+i
print("Orginal Word is: ",line)
print("The Togglecase Word is:",line2)