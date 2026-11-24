# STRINGS, COLLECTIONS AND FUNCTIONS

# topic cuvered:
#6	6(a)	Character and Word Count
#7	5(a)	Armstrong and Palindrome
#8	5(c)	Lambda Function
#9	8(a)	Tuple – Circle Area
#10	7(b)	Dictionary Sorting
#11	5(b)	Recursive Factorial

#6. Character and Word Count

text = input("Enter a string:")

characters = len(text)
word = len(text.split())

print("Number of characters.",characters)
print("Number of word:",word)




#7. Armstrong and Palindrome

def is_armstrong(num):
    if num < 0:
        return False

    digits = str(num)  # Convert number into string
    power = len(digits)  # Count number of digits
    total = sum(int(digit)**power for digit in digits)  # Calculate sum

    return total == num  # Check Armstrong condition


# 2. Palindrome Number
def is_palindrome(num):
    text = str(num)  # Convert number into string
    return text == text[::-1]  # Compare original and reversed number


# Test
n = int(input("Enter a number: "))

if is_armstrong(n):
    print(n, "is an Armstrong number.")
else:
    print(n, "is not an Armstrong number.")

if is_palindrome(n):
    print(n, "is a palindrome.")
else:
    print(n, "is not a palindrome.")




#8. Lambda Function


# Check if String Starts with a Character
# Program to check whether a string starts with a given character.

start_with = lambda text, ch: text.startswith(ch)  # Check starting character

character = input("Enter the character to check: ")

if len(character) != 1:  # Check exactly one character
    print("Please enter exactly one character.")
else:
    string = input("Enter a string: ")
    print(start_with(string, character))  # Call the lambda function

# Important:
# lambda = Creates a small anonymous function
# startswith() = Checks the starting character
# len() = Counts characters
# != 1 = Checks whether length is not equal to 1



#9. Tuple – Circle Area


#  Area and Circumference of Circle
# Program to calculate area and circumference using radius.

import math  # Import math module for pi value

def circle(radius):
    area = math.pi * radius ** 2  # Calculate area
    circumference = 2 * math.pi * radius  # Calculate circumference
    return area, circumference  # Return both values as a tuple


# Test
r = float(input("Enter the radius: "))

if r < 0:
    print("Radius cannot be negative.")
else:
    area, circumference = circle(r)  # Get returned values

    print("Area of circle:", area)
    print("Circumference of circle:", circumference)
    print("Returned tuple:", circle(r))

# Important:
# math.pi = Value of pi (3.14159...)
# ** 2 = Square of radius
# return = Returns both values
# Tuple = Stores multiple values together



#10. Dictionary Sorting

marks = {
    "Rahul":85,
    "Priya":92,
    "Amit":75,
    "Scha":88,
}

ascending = dict(sorted(marks.items(),key = lambda item : item [1]))
descending = dict(sorted(marks.items(),key = lambda item : item [1], reverse = True))

print("original dictionary :", marks)
print("Ascending order :", ascending)
print("decending order :", descending)

#11. Recursive Factorial


# 19. Factorial Using Recursion
# Program to calculate factorial of a number.

def factorial(n):
    if n < 0:
        return None  # Negative numbers are not allowed

    if n == 0 or n == 1:
        return 1  # Base condition

    return n * factorial(n - 1)  # Recursive function call


# Test
num = int(input("Enter a non-negative integer:"))

result = factorial(num)  # Call factorial function

if result is None:
    print("Factorial is not defined for negative integers.")
else:
    print("Factorial of", num, "is", result)


# Important:
# Recursion = Function calling itself
# Base condition = Stops recursion
# factorial(5) = 5 * 4 * 3 * 2 * 1 = 120
