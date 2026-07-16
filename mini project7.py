# Student Profile Manager

# Taking input from the user
student = {
    "Name": input("Enter Name: "),
    "Age": int(input("Enter Age: ")),
    "Course": input("Enter Course: "),
    "College": input("Enter College: "),
    "City": input("Enter City: ")
}

# Display Student Profile
print("\n===== STUDENT PROFILE =====")
for key, value in student.items():
    print(f"{key} : {value}")

# Update one field
field = input("\nEnter the field you want to update (Name/Age/Course/College/City): ")

if field in student:
    new_value = input(f"Enter new value for {field}: ")

    if field == "Age":
        student[field] = int(new_value)
    else:
        student[field] = new_value

    print("\nProfile Updated Successfully!")
else:
    print("Field not found!")

# Delete one field
delete_field = input("\nEnter the field you want to delete: ")

if delete_field in student:
    student.pop(delete_field)
    print(f"{delete_field} deleted successfully!")
else:
    print("Field not found!")

# Print Updated Student Profile
print("\n===== UPDATED STUDENT PROFILE =====")
for key, value in student.items():
    print(f"{key} : {value}")

# Print all keys
print("\nAll Keys:")
print(student.keys())

# Print all values
print("\nAll Values:")
print(student.values())

# Print total fields
print("\nTotal Fields:", len(student))