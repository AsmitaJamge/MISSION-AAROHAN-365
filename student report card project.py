# ==========================================
#      STUDENT REPORT CARD SYSTEM
#        Created by Asmita Jamge
# ==========================================


# -------- Student Information --------
def student_info():
    print("\n========== STUDENT INFORMATION ==========")
    name = input("Enter Student Name : ")
    roll = input("Enter Roll Number : ")
    course = input("Enter Course : ")
    return name, roll, course


# -------- Total Marks --------
def total_marks(m1, m2, m3, m4, m5):
    return m1 + m2 + m3 + m4 + m5


# -------- Percentage --------
def percentage(total):
    return total / 5


# -------- Grade --------
def grade(per):
    if per >= 90:
        return "A+"
    elif per >= 80:
        return "A"
    elif per >= 70:
        return "B"
    elif per >= 60:
        return "C"
    elif per >= 40:
        return "D"
    else:
        return "Fail"


# -------- Scholarship --------
def scholarship(per):
    if per >= 90:
        return "100% Scholarship"
    elif per >= 80:
        return "50% Scholarship"
    elif per >= 70:
        return "25% Scholarship"
    else:
        return "No Scholarship"


# ================= MAIN PROGRAM =================

name, roll, course = student_info()

print("\nEnter Marks (Out of 100)")

m1 = float(input("Python : "))
m2 = float(input("DBMS : "))
m3 = float(input("Web Technology : "))
m4 = float(input("Mathematics : "))
m5 = float(input("English : "))

total = total_marks(m1, m2, m3, m4, m5)
per = percentage(total)
g = grade(per)
sch = scholarship(per)

print("\n=========================================")
print("          STUDENT REPORT CARD")
print("=========================================")

print("Name        :", name)
print("Roll No     :", roll)
print("Course      :", course)

print("-----------------------------------------")
print("Python          :", m1)
print("DBMS            :", m2)
print("Web Technology  :", m3)
print("Mathematics     :", m4)
print("English         :", m5)

print("-----------------------------------------")
print("Total Marks :", total, "/500")
print("Percentage  :", round(per, 2), "%")
print("Grade       :", g)
print("Scholarship :", sch)
print("=========================================")