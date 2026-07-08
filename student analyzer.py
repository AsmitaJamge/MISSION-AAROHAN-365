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

total_marks= mark1+mark2+mark3
print("Total Marks:",total_marks)

avg=total_marks/3
print("Average Marks:",avg)

if mark1>=90 and mark2>=90 and mark3>=90:
    print("Grade:A")
elif mark1>=70 and mark2>=70 and mark3>=70:
    print("Grade:B")
elif mark1>=50 and mark2>=50 and mark3>=50:
    print("Grade:C")
elif mark1>=35 and mark2>=35 and mark3>=35:
    print("Grade:D")
else:
    print("Fail")

if age>=18:
    if age<0:
        print("Invalid age")
    print("Voting : Eligible for voting")
else:
    print("Voting : Not eligible for voting" )

if total_marks>=75:
    print("Scolarship:You selected for scolarship")
else:
    print("Scolarship:You not selected for scolarship")

print("="*40)

