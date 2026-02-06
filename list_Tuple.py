# Simple Interest Calculator
p = int(input("Enter Principal: "))
r = float(input("Enter Rate of interest: "))
t = int(input("Enter Time in years: "))

si = (p * r * t) / 100
print("The interest is", si)



# Leap Year Test
year = int(input("Enter the year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("The year", year, "is a leap year")
else:
    print("The year", year, "is not a leap year")



# Inverted Right-Angled Triangle Pattern
for i in range(5, 0, -1):
    print("*" * i)




# Menu-Driven Calculator
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
choice = int(input("Enter your choice:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n"))

match choice:
    case 1:
        print("Result:", first + second)
    case 2:
        print("Result:", first - second)
    case 3:
        print("Result:", first * second)
    case 4:
        print("Result:", first / second)
    case _:
        print("Invalid Choice")



