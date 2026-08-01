# ==========================================
# Python Assignment - Basics to Type Casting
# ==========================================


# ------------------------------------------
# Q1. Which of the following identifier names
# are invalid? Give the reason.
#
# Serial_no
# 1st_Room
# Hundred7
# Total_Mark3
# total-Mark3
# Total Marks
# Tru#
# _Percentage
# ------------------------------------------

# Valid:
# Serial_no
# Hundred7
# Total_Mark3
# _Percentage

# Invalid:
# 1st_Room   -> Cannot start with a number
# total-Mark3 -> '-' is not allowed
# Total Marks -> Space is not allowed
# Tru#        -> '#' is not allowed


# ------------------------------------------
# Q2. Write Python statements:
#
# 1. Assign 10 to length and 20 to breadth.
# 2. Store the average in a variable avg.
# 3. Create a list named stationery.
# 4. Store Mohandas, Karamchand and Gandhi
#    into first, middle and last.
# 5. Create fullname by joining them.
# ------------------------------------------

length = 10
breadth = 20

avg = (length + breadth) / 2

stationery = ["Paper", "Gel Pen", "Eraser"]

first = "Mohandas"
middle = "Karamchand"
last = "Gandhi"

fullname = first + " " + middle + " " + last

print("Average =", avg)
print("Full Name =", fullname)


# ------------------------------------------
# Q3. Theory
#
# What is the difference between
# Static Typing and Dynamic Typing?
# ------------------------------------------

# Static Typing:
# Data type is declared explicitly before using a variable.
# Example: C, C++, Java

# Dynamic Typing:
# Python automatically determines the data type at runtime.
# Example:
# x = 10
# x = "Hello"


# ------------------------------------------
# Q4.
#
# Given:
# name = ["Mohan", "dash", "karam",
#         "chandra", "gandhi", "Bapu"]
#
# 1. Insert "freedom_fighter" at index 0.
# 2. Add "NetaJi" and "Bose" at the end.
# ------------------------------------------

name = ["Mohan", "dash", "karam", "chandra", "gandhi", "Bapu"]

name.insert(0, "freedom_fighter")

name.append("NetaJi")
name.append("Bose")

print(name)


# ------------------------------------------
# Q5.
#
# Find the output.
# ------------------------------------------

name = ["Bapuji", "dash", "karam", "chandra", "gandhi", "Mohan"]

temp = name[-1]
name[-1] = name[0]
name[0] = temp

print(name)

# Output:
# ['Mohan', 'dash', 'karam', 'chandra', 'gandhi', 'Bapuji']


# ------------------------------------------
# Q6.
#
# Find the output.
# ------------------------------------------

name = [
    "freedomFighter",
    "Bapuji",
    "Mohan",
    "dash",
    "karam",
    "chandra",
    "gandhi"
]

length1 = len(name[-len(name)+1:-1:2])
length2 = len(name[-len(name)+1:-1])

print(length1 + length2)

# Output: 8


# ------------------------------------------
# Q7.
#
# Find the output.
# ------------------------------------------

animal = ['Human', 'cat', 'mat', 'cat', 'rat', 'Human', 'Lion']

print(animal.count("Human"))   # 2
print(animal.index("rat"))     # 4
print(len(animal))             # 7


# ------------------------------------------
# Q8.
#
# Given:
# tuple1 = (
#     10,
#     20,
#     "Apple",
#     3.4,
#     'a',
#     ["master","ji"],
#     ("sita","geeta",22),
#     [{"roll_no":1},{"name":"Navneet"}]
# )
#
# 1. Find length.
# 2. Print "Navneet".
# 3. Print roll_no.
# 4. Print tuple1[-3][1].
# 5. Print 22.
# ------------------------------------------

tuple1 = (
    10,
    20,
    "Apple",
    3.4,
    'a',
    ["master", "ji"],
    ("sita", "geeta", 22),
    [{"roll_no": 1}, {"name": "Navneet"}]
)

print(len(tuple1))

print(tuple1[7][1]["name"])

print(tuple1[7][0]["roll_no"])

print(tuple1[-3][1])

print(tuple1[6][2])


# ------------------------------------------
# Q9. Theory
#
# 1. What are the three numeric data types?
# 2. Give one example of each.
# ------------------------------------------

# int     -> 10
# float   -> 10.5
# complex -> 4 + 3j


# ------------------------------------------
# Q10. Theory
#
# 1. How is Boolean related to Integer?
# 2. Significance of True and False?
# ------------------------------------------

# True behaves like 1
# False behaves like 0

# Boolean is mainly used for decision making
# (if, while, comparisons).


# ------------------------------------------
# Q11. Theory
#
# 1. What are Sequence Data Types?
# 2. Difference between List and Tuple.
# ------------------------------------------

# Sequence Data Types:
# String, List and Tuple

# List:
# - Mutable
# - Uses []

# Tuple:
# - Immutable
# - Uses ()


# ------------------------------------------
# Q12. Theory
#
# 1. What is a Set?
# 2. Difference between Set and List?
# 3. What is FrozenSet?
# ------------------------------------------

# Set:
# An unordered collection of unique elements.

# List vs Set
# List -> Ordered, duplicates allowed.
# Set  -> Unordered, duplicates not allowed.

# FrozenSet:
# An immutable version of a set.


# ------------------------------------------
# Q13. Theory
#
# 1. How is Dictionary different from
#    other data types?
# 2. Dictionary syntax.
# 3. Significance of Keys and Values.
# 4. Explain:
#    pop()
#    popitem()
#    clear()
# ------------------------------------------

# Dictionary stores data in key-value pairs.

# Syntax:
# student = {"name": "Steve", "age": 20}

# Keys identify values.
# Keys must be unique and immutable.

student = {
    "name": "Steve",
    "age": 20,
    "country": "India"
}

student.pop("age")
print(student)

student.popitem()
print(student)

student.clear()
print(student)


# ------------------------------------------
# Q14. Theory
#
# Differentiate between Mutable and
# Immutable data types with examples.
# ------------------------------------------

# Mutable:
# Can be modified after creation.
# Examples:
# List, Dictionary, Set

# Immutable:
# Cannot be modified after creation.
# Examples:
# String, Tuple, Integer, Float, Boolean