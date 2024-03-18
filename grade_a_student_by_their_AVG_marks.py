print("Grade a Student by their Marks")
tamil=int(input("Marks you've Scored in Tamil: "))
english=int(input("Marks you've Scored in English: "))
maths=int(input("Marks you've Scored in Maths: "))
science=int(input("Marks you've Scored in Science: "))
social_science=int(input("Marks you've Scored in Social Science: "))
mark=(tamil+english+maths+science+social_science)/5
if mark == 100 or mark >= 90:
    print("You got a 'A'-Grade with",mark)
elif mark == 89 or mark >= 80:
    print("You got a 'B'-Grade with",mark)
elif mark == 79 or mark >= 70:
    print("You got a 'C'-Grade with",mark)
elif mark == 69 or mark >= 50:
    print("You got a 'D'-Grade with",mark)
elif mark == 49 or mark >= 35:
    print("You Just Passed with",mark)
else:
    print("You Failed..!!")