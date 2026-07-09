# Student ID Card Generator using Functions

# Function to take student information
def student_info():
    name = input("Enter Student Name: ")
    roll = input("Enter Roll Number: ")
    course = input("Enter Course: ")
    college = input("Enter College Name: ")
    city = input("Enter City: ")

    return name, roll, course, college, city


# Function to display ID Card
def display_card(name, roll, course, college, city):
    print("\n")
    print("=" * 40)
    print("         STUDENT ID CARD")
    print("=" * 40)
    print("Name      :", name)
    print("Roll No.  :", roll)
    print("Course    :", course)
    print("College   :", college)
    print("City      :", city)
    print("=" * 40)


# Main Program
name, roll, course, college, city = student_info()
display_card(name, roll, course, college, city)