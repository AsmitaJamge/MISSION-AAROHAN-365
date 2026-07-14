<<<<<<< HEAD
# list 

# ==============================
# PYTHON LIST - ALL CONCEPTS
# ==============================

# 1. Creating a List
fruits = ["Apple", "Banana", "Mango", "Orange"]

print("Original List:")
print(fruits)

# ------------------------------
# 2. Accessing Elements
# ------------------------------

print("\nFirst Fruit:", fruits[0])
print("Second Fruit:", fruits[1])
print("Last Fruit:", fruits[-1])

# ------------------------------
# 3. Updating List
# ------------------------------

fruits[1] = "Grapes"

print("\nAfter Updating:")
print(fruits)

# ------------------------------
# 4. Adding Elements
# ------------------------------

fruits.append("Pineapple")      # Add at end
fruits.insert(1, "Kiwi")        # Add at index 1

print("\nAfter Adding:")
print(fruits)

# ------------------------------
# 5. Removing Elements
# ------------------------------

fruits.remove("Apple")          # Remove by value
fruits.pop()                    # Remove last element
del fruits[1]                   # Remove by index

print("\nAfter Removing:")
print(fruits)

# ------------------------------
# 6. List Length
# ------------------------------

print("\nTotal Fruits:", len(fruits))

# ------------------------------
# 7. Loop Through List
# ------------------------------

print("\nUsing for loop:")

for fruit in fruits:
    print(fruit)

# ------------------------------
# 8. Check Item Exists
# ------------------------------

if "Mango" in fruits:
    print("\nMango is Present")
else:
    print("\nMango is Not Present")

# ------------------------------
# 9. Sorting
# ------------------------------

numbers = [40, 10, 50, 20, 30]

numbers.sort()

print("\nAscending Order:")
print(numbers)

numbers.sort(reverse=True)

print("Descending Order:")
print(numbers)

# ------------------------------
# 10. Reverse List
# ------------------------------

numbers.reverse()

print("\nReverse List:")
print(numbers)

# ------------------------------
# 11. Copy List
# ------------------------------

new_numbers = numbers.copy()

print("\nCopied List:")
print(new_numbers)

# ------------------------------
# 12. Concatenate Lists
# ------------------------------

list1 = [1, 2, 3]
list2 = [4, 5, 6]

list3 = list1 + list2

print("\nCombined List:")
print(list3)

# ------------------------------
# 13. Count Elements
# ------------------------------

marks = [90, 80, 90, 70, 90]

print("\n90 appears:", marks.count(90), "times")

# ------------------------------
# 14. Index of Element
# ------------------------------

print("Index of 80:", marks.index(80))

# ------------------------------
# 15. Clear List
# ------------------------------

temp = [1, 2, 3]

temp.clear()

print("\nAfter Clear:")
print(temp)

# ------------------------------
# 16. List Slicing
# ------------------------------

numbers = [10,20,30,40,50,60]

print("\nOriginal:", numbers)
print("First 3:", numbers[:3])
print("Last 3:", numbers[-3:])
print("Middle:", numbers[2:5])

# ------------------------------
# 17. Nested List
# ------------------------------

students = [
    ["Asmita", 90],
    ["Rahul", 85],
    ["Sneha", 95]
]

print("\nNested List:")

for student in students:
    print(student[0], "-", student[1])

# ------------------------------
# 18. Sum, Max, Min
# ------------------------------

nums = [10,20,30,40,50]

print("\nSum =", sum(nums))
print("Maximum =", max(nums))
print("Minimum =", min(nums))

# ------------------------------
# 19. User Input List
# ------------------------------

numbers = []

n = int(input("\nHow many numbers do you want to enter? "))

for i in range(n):
    num = int(input("Enter Number: "))
    numbers.append(num)

print("Your List:", numbers)
print("Total:", sum(numbers))

# ------------------------------
# 20. List Comprehension
# ------------------------------

square = [x*x for x in range(1,6)]

print("\nSquares:")
print(square)

# ==============================
# END OF PROGRAM
=======
# list 

# ==============================
# PYTHON LIST - ALL CONCEPTS
# ==============================

# 1. Creating a List
fruits = ["Apple", "Banana", "Mango", "Orange"]

print("Original List:")
print(fruits)

# ------------------------------
# 2. Accessing Elements
# ------------------------------

print("\nFirst Fruit:", fruits[0])
print("Second Fruit:", fruits[1])
print("Last Fruit:", fruits[-1])

# ------------------------------
# 3. Updating List
# ------------------------------

fruits[1] = "Grapes"

print("\nAfter Updating:")
print(fruits)

# ------------------------------
# 4. Adding Elements
# ------------------------------

fruits.append("Pineapple")      # Add at end
fruits.insert(1, "Kiwi")        # Add at index 1

print("\nAfter Adding:")
print(fruits)

# ------------------------------
# 5. Removing Elements
# ------------------------------

fruits.remove("Apple")          # Remove by value
fruits.pop()                    # Remove last element
del fruits[1]                   # Remove by index

print("\nAfter Removing:")
print(fruits)

# ------------------------------
# 6. List Length
# ------------------------------

print("\nTotal Fruits:", len(fruits))

# ------------------------------
# 7. Loop Through List
# ------------------------------

print("\nUsing for loop:")

for fruit in fruits:
    print(fruit)

# ------------------------------
# 8. Check Item Exists
# ------------------------------

if "Mango" in fruits:
    print("\nMango is Present")
else:
    print("\nMango is Not Present")

# ------------------------------
# 9. Sorting
# ------------------------------

numbers = [40, 10, 50, 20, 30]

numbers.sort()

print("\nAscending Order:")
print(numbers)

numbers.sort(reverse=True)

print("Descending Order:")
print(numbers)

# ------------------------------
# 10. Reverse List
# ------------------------------

numbers.reverse()

print("\nReverse List:")
print(numbers)

# ------------------------------
# 11. Copy List
# ------------------------------

new_numbers = numbers.copy()

print("\nCopied List:")
print(new_numbers)

# ------------------------------
# 12. Concatenate Lists
# ------------------------------

list1 = [1, 2, 3]
list2 = [4, 5, 6]

list3 = list1 + list2

print("\nCombined List:")
print(list3)

# ------------------------------
# 13. Count Elements
# ------------------------------

marks = [90, 80, 90, 70, 90]

print("\n90 appears:", marks.count(90), "times")

# ------------------------------
# 14. Index of Element
# ------------------------------

print("Index of 80:", marks.index(80))

# ------------------------------
# 15. Clear List
# ------------------------------

temp = [1, 2, 3]

temp.clear()

print("\nAfter Clear:")
print(temp)

# ------------------------------
# 16. List Slicing
# ------------------------------

numbers = [10,20,30,40,50,60]

print("\nOriginal:", numbers)
print("First 3:", numbers[:3])
print("Last 3:", numbers[-3:])
print("Middle:", numbers[2:5])

# ------------------------------
# 17. Nested List
# ------------------------------

students = [
    ["Asmita", 90],
    ["Rahul", 85],
    ["Sneha", 95]
]

print("\nNested List:")

for student in students:
    print(student[0], "-", student[1])

# ------------------------------
# 18. Sum, Max, Min
# ------------------------------

nums = [10,20,30,40,50]

print("\nSum =", sum(nums))
print("Maximum =", max(nums))
print("Minimum =", min(nums))

# ------------------------------
# 19. User Input List
# ------------------------------

numbers = []

n = int(input("\nHow many numbers do you want to enter? "))

for i in range(n):
    num = int(input("Enter Number: "))
    numbers.append(num)

print("Your List:", numbers)
print("Total:", sum(numbers))

# ------------------------------
# 20. List Comprehension
# ------------------------------

square = [x*x for x in range(1,6)]

print("\nSquares:")
print(square)

# ==============================
# END OF PROGRAM
>>>>>>> 0c307c4c5ec2aa998e1888e94827c3509a708bed
# ==============================