#Task 1: Variables and Data Types Create variables to store a person's name (string), age (integer), height in meters (float), and whether they are a student (boolean). Print all four values in a single print() statement.

#Task 2: String Formatting Using the variables from Task 1, print a sentence in the following format: Name: <name> | Age: <age> | Height: <height> | Student: <is_student>

#Task 3: Arithmetic Operations Using the age variable, calculate and print:
# Age in months
# Age in days (assume 365 days/year)
# The remainder when age is divided by 7
# Age raised to the power of 2

#Task-1:
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height(in m): "))
is_student = bool(input("Are you a student?(True or False): "))
print(name,age,height,is_student)
 
#Task-2:
print(f"Name: {name} | Age: {age} | Height: {height} | Student: {is_student}")

#Task-3:
age_months = age*12
age_days = age*365
rem = age%7
power = age**2
print(age_months,age_days,rem,power)