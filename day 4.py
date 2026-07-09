# Topic 1:comparison operator
print(10>5)
print(20<10)
print(15 == 15)
print(5!=5)


#Topic 2: boolean
age=19
print(age>=18)
print(age<=18)


#Topic 3: if statement
age=20
if age>=18:
    print("You can vote.")


#Topic 4:if - else
age = int(input("Enter your age:"))
if age >= 18:
    print("Eligible for voting")
else:
    print("Not eligible for voting")


#Topic 5: elif
marks = int(input("Enter your marks: "))
if marks>=90:
    print("grade:A")
elif marks>=70:
    print("grade:B")
elif marks>=50:
    print("grade:C")
else:
    print("Fail")
