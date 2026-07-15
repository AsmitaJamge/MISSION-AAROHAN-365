# ==============================
# Student Skills Manager
# ==============================

# Create a Set of programming skills
skills = {"Python", "C", "Java", "HTML"}

print("Initial Skills:", skills)

# Add new skills
new_skill = input("\nEnter a new skill to add: ")
skills.add(new_skill)
print("Skills after adding:", skills)

# Remove one skill
remove_skill = input("\nEnter a skill to remove: ")

if remove_skill in skills:
    skills.remove(remove_skill)
    print(remove_skill, "removed successfully.")
else:
    print(remove_skill, "not found in the set.")

# Check whether Python exists
print("\nChecking for Python...")

if "Python" in skills:
    print("✅ Python is available in the skills set.")
else:
    print("❌ Python is not available.")

# Print all unique skills
print("\nAll Unique Skills:")
for skill in skills:
    print("-", skill)

# Print total number of skills
print("\nTotal Skills:", len(skills))