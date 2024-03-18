year=int(input("Enter a Year to find Leap or Not: "))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("Given year is an Leap Year")
        else:
            print("Given year is an Not a Leap Year")
    else:
        print("Given year is an Leap Year")
else:
     print("Given year is an Not a Leap Year")