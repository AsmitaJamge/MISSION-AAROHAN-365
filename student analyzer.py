#STUDENT RESULT MANAGEMENT SYSTEM
student_name = input("Enter your  Full Name:")
age = int(input("Enter your Age:"))
city = input("Enter your City:")
course =input("Enter your Course:")
mark1=int(input("Enter python marks:"))
mark2=int(input("Enter english marks:"))
mark3 = int(input("Enter math marks:"))

print("="*40)
print("           STUDENT REPORT         ")
print("="*40)

print("Name:",student_name)
print("Age:",age)
print("City:",city)
print("Course:",course)
print("Python:",mark1)
print("English:",mark2)
print("Math:",mark3)

total_marks= 300
print("Total Marks:",total_marks)

gain_mark=mark1+mark2+mark3
print("Gain marks:",gain_mark)

percentage=gain_mark/total_marks*100
print("Percentage Marks:",percentage)

if percentage>=90:
    print("Grade:A")
elif percentage>=70:
    print("Grade:B")
elif percentage>=50:
    print("Grade:C")
elif percentage>=35:
    print("Grade:D")
else:
    print("Fail")

if age>=18:
    print("Voting : Eligible for voting")
else:
    print("Voting : Not eligible for voting" )

if percentage>=75:
    print("Scolarship:You selected for scolarship")
else:
    print("Scolarship:You not selected for scolarship")

print("="*40)

