#Task 1: Perform Basic Mathematical Operations
#Problem Statement: Write a Python program that does the following:
#1.  Takes two numbers as input from the user.
#2.  Performs the basic mathematical operations on these two numbers:
#o	Addition
#o	Subtraction
#o	Multiplication
#o	Division
#3.  Displays the results of each operation on the screen.


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
if num2 != 0:
    division = num1 / num2
else:
    division = "Undefined (division by zero)"
print("\nResults:")
print(f"Addition: {num1} + {num2} = {addition}")
print(f"Subtraction: {num1} - {num2} = {subtraction}")
print(f"Multiplication: {num1} * {num2} = {multiplication}")
print(f"Division: {num1} / {num2} = {division}")
