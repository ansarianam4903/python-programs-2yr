# DAY 01 OF PYTHON PROGRAM 
# 1.Odd and Even program:

num = int(input("Enter a number:"))

if num % 2 == 0:
 print(num,"is an Even number.")
else:
 print(num,"is an odd number.")

# 2.SGPI GRADE:

sgpi = float(input("Enter your SGPI :"))

if sgpi <0 or sgpi >10:
    print("invalid SGPI.Enter a value between 0 and 10:")
elif sgpi >=9.00:
    print("Grade:O")
elif sgpi >=8.00:
    print("Grade:A+")
elif sgpi >=7.00:
    print("Grade:A")
elif sgpi >=6.00:
    print("Grade:B+")
elif sgpi >=5.50:
    print("Grade:B")
elif sgpi >=5.00:
    print("Grade:C")
elif sgpi >=4.00:
    print("Grade:P")
else:
    print("Grade:F")

# 3.AGE CALCULATOR:

from datetime import date

name = input("Enter your name:")
age = int(input("Enter your age:"))

current_year = date.today().year
year_100 = current_year + (100-age)

print(f"Hello {name}!")
print(f"you will turn 100 years old in the year{year_100}.")

# 4.fibonacci series:

n =int(input("Enter the number of terms:"))

if n<=0:
   print("Enter a positive integer.")
else:
   a,b=0,1

print("fibonacci series:")

for i in range (n): 
 print( a,end ="")
 a,b = b, a+b

print()

# 5.sum of digit of a number:

num = abs(int(input("Enter a number: ")))  # Convert negative number to positive
total = 0  # Initialize sum as 0

while num > 0:  # Loop runs until number becomes 0
    digit = num % 10  # Get the last digit
    total += digit  # Add digit to total
    num //= 10  # Remove the last digit

print("Sum of digits:", total)  # Display final sum

# Example: 1234 → 1 + 2 + 3 + 4 = 10
# Important:
# % 10  = Gets the last digit
# // 10 = Removes the last digit
# +=    = Adds value to total

# Output:
# Enter a number: 1234
# Sum of digits: 10
