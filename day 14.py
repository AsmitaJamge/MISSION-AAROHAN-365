# Create a dictionary of a student
student = {
    "name": "Asmita",
    "age": 19,
    "course": "B.Sc. Computer Science"
}

# Print name and age
print("Name:", student["name"])
print("Age:", student["age"])

# Add city
student["city"] = "Nanded"
print("\nAfter adding city:")
print(student)

# Update course
student["course"] = "Python Full Stack Development"
print("\nAfter updating course:")
print(student)

# Remove age
student.pop("age")
print("\nAfter removing age:")
print(student)

# Print all keys
print("\nKeys:")
print(student.keys())

# Print all values
print("\nValues:")
print(student.values())

# Print key-value pairs using loop
print("\nKey-Value Pairs:")
for key, value in student.items():
    print(key, ":", value)

# Check whether "name" exists
if "name" in student:
    print("\n'name' key exists.")
else:
    print("\n'name' key does not exist.")

# Copy dictionary
student_copy = student.copy()

print("\nCopied Dictionary:")
print(student_copy)