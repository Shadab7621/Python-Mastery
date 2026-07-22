# ==========================================
# Assignment 01 - Variables & Input/Output
# ==========================================

# -----------------------------
# Q1. Assign 10 to variable length and 20 to variable breadth.
# -----------------------------

length = 10
breadth = 20


# -----------------------------
# Q2. Store the average of length and breadth in a variable named avg.
# -----------------------------

avg = (length + breadth) / 2
print("Average:", avg)


# -----------------------------
# Q3. Create a list named stationery containing:
# Paper, Gel Pen, Eraser
# -----------------------------

stationery = ["Paper", "Gel Pen", "Eraser"]
print(stationery)


# -----------------------------
# Q4. Store first, middle and last names separately.
# -----------------------------

first = "Mohandas"
middle = "Karamchand"
last = "Gandhi"

print(first)
print(middle)
print(last)


# -----------------------------
# Q5. Create fullname by joining first, middle and last names.
# -----------------------------

fullname = first + " " + middle + " " + last
print(fullname)


# ==========================================
# Theory Questions (Interview Practice)
# ==========================================

# Q1. What is a variable?
# Ans:
# A variable is a name used to store a value in memory.


# Q2. What is Dynamic Typing?
# Ans:
# Python automatically determines the datatype of a variable.
# No datatype declaration is required.


# Q3. Difference between Static Typing and Dynamic Typing?
#
# Static Typing
# - Datatype declared manually.
# - Used in C, C++, Java.
#
# Dynamic Typing
# - Datatype detected automatically.
# - Used in Python.


# Q4. Why is Python called a dynamically typed language?
# Ans:
# Because Python automatically assigns the datatype at runtime.


# Q5. Is Python case-sensitive?
# Ans:
# Yes.
#
# age = 20
# Age = 30
#
# Both are different variables.


# Q6. Why should keywords not be used as variable names?
# Ans:
# Keywords have predefined meanings in Python.
# Using them as variable names causes an error.


# Q7. What are the rules for naming variables?
# Ans:
# - Can contain letters, digits and underscore (_)
# - Cannot start with a digit
# - Cannot contain spaces
# - Cannot contain special characters
# - Cannot use Python keywords
# - Variable names are case-sensitive


# Q8. What is help()?
# Ans:
# help() displays documentation of Python functions, modules or objects.


# Q9. What are comments?
# Ans:
# Comments are ignored by Python and are used to explain code.
#
# Single-line:
#   # Comment
#
# Multi-line:
#   """
#   Comment
#   """


# Q10. What does input() do?
# Ans:
# input() is used to take input from the user.


# Q11. What datatype does input() return?
# Ans:
# input() always returns a string (str).


# Q12. What is print() used for?
# Ans:
# print() displays output on the screen.


# Q13. What is an f-string?
# Ans:
# An f-string is the preferred way to insert variables into strings.
#
# Example:
# print(f"My name is {name}")


# Q14. What is sep used for?
# Ans:
# sep changes the separator between multiple values.


# Q15. What is end used for?
# Ans:
# end changes what is printed after the output.
# Default is a new line (\n).


# Q16. Which identifiers are invalid and why?
#
# Serial_no      -> Valid
# 1st_Room       -> Invalid (Starts with a digit)
# Hundred7       -> Valid
# Total_Mark3    -> Valid
# total-Mark3    -> Invalid (- not allowed)
# Total Marks    -> Invalid (Space not allowed)
# Tru#           -> Invalid (# not allowed)
# _Percentage    -> Valid