name = input("Enter your name: ")
age = int(input("Enter your age: "))
roll_number = input("Enter your roll number: ")
sub1 = input("Enter the name of subject 1: ")
sub2 = input("Enter the name of subject 2: ")
sub3 = input("Enter the name of subject 3: ")
sub4 = input("Enter the name of subject 4: ")
sub5 = input("Enter the name of subject 5: ")
marks = []
for i in range(5):
    mark = int(input(f"Enter marks for subject {i+1}: "))
    marks.append(mark)
Total_marks = 500
gain_mark = sum(marks)

average = gain_mark / Total_marks * 100
print("\nStudent Report")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Roll Number: {roll_number}")
print(f"Subject 1: {sub1}")
print(f"Subject 2: {sub2}")
print(f"Subject 3: {sub3}")
print(f"Subject 4: {sub4}")
print(f"Subject 5: {sub5}")
print(f"Gain marks: {gain_mark}")
print(f"Average Marks: {average:.2f}")

                          
                    