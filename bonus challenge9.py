# Create Dictionary

employees = {
    "E101": "Asmita",
    "E102": "Rahul",
    "E103": "Sneha"
}

# Print Employee IDs
print("Employee IDs:")
print(employees.keys())

# Print Employee Names
print("\nEmployee Names:")
print(employees.values())

# Check E102
if "E102" in employees:
    print("\nE102 exists.")
else:
    print("\nE102 does not exist.")

# Add E104
employees["E104"] = "Priya"
print("\nAfter Adding E104:")
print(employees)

# Remove E101
employees.pop("E101")
print("\nAfter Removing E101:")
print(employees)

# Loop through Dictionary
print("\nEmployee Details:")
for emp_id, name in employees.items():
    print(emp_id, ":", name)

# Total Employees
print("\nTotal Employees:", len(employees))