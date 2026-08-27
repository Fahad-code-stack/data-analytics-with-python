# Part -1 Python Basics (Variables)
# Print name, father name, and date of birth using escape sequences
print("Name:\tFahad Mumtaz")
print("Father Name:\tIrfan Mumtaz")
print("Date of Birth:\t10-02-2005")

# Part -2 Small Bio using Variables

name = "Fahad Mumtaz"
father_name = "Irfan Mumtaz"
date_of_birth = "10-02-2005"
education = "Python Student"
hobby = "Learning Data Analytics"

print("Name:", name)
print("Father Name:", father_name)
print("Date of Birth:", date_of_birth)
print("Education:", education)
print("Hobby:", hobby)

# Part -3 Python Operators

a = 10
b = 3

# Arithmetic operators
print("\nArithmetic Operators:")
print(a + b)       # Addition
print(a - b)       # Subtraction
print(a * b)       # Multiplication
print(a / b)       # Division
print(a // b)      # Floor division
print(a % b)       # Modulus
print(a ** b)      # Exponentiation
print([[1, 2]] @ [[3], [4]])  # Matrix multiplication

# Assignment operators
a += 2
a -= 1
a *= 2
a /= 2
a //= 2
a %= 3
a **= 2
print("\nAssignment result:", a)

# Comparison operators
print("\nComparison Operators:")
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

# Logical operators
print("\nLogical Operators:")
print(a > 0 and b > 0)
print(a > 0 or b < 0)
print(not(a == b))

# Bitwise operators
print("\nBitwise Operators:")
print(a & b)
print(a | b)
print(a ^ b)
print(~a)
print(a << 1)
print(a >> 1)

# Identity operators
x = [1, 2]
y = x
print("\nIdentity Operators:")
print(x is y)
print(x is not y)

# Membership operators
print("\nMembership Operators:")
print(2 in x)
print(5 not in x)

# Conditional expression
result = "a is greater" if a > b else "b is greater"
print("\nConditional Operator:", result)

# Part -4 Marks and Percentage

english_marks = 85
islamiat_marks = 90
maths_marks = 95

total_marks = 300
obtained_marks = english_marks + islamiat_marks + maths_marks
percentage = (obtained_marks / total_marks) * 100

print("\nMarks and Percentage:")
print("Obtained Marks:", obtained_marks)
print("Total Marks:", total_marks)
print("Percentage:", percentage, "%")