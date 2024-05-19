
#Question15
import datetime

# Get current date and time
current_datetime = datetime.datetime.now()

# Extract full month name
full_month_name = current_datetime.strftime("%B")

print("Current Date and Time:", current_datetime)
print("Full Month Name:", full_month_name)

#Question16
def greet(name, day="Sunday"):
    print(f"Hi {name}! Happy {day}!")

# Invoking the function with two variables
greet("Alice", "Wednesday")

# Invoking the function with one variable
greet("Bob")

#Question17
# Define a function to perform division
def divide_numbers(dividend, divisor):
    try:
        result = dividend / divisor
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    else:
        print("Division successful! Result:", result)
    finally:
        print("Division operation completed.")

# Test the function with different scenarios
# Scenario 1: Dividing by a non-zero number
print("Scenario 1:")
divide_numbers(10, 2)

# Scenario 2: Dividing by zero (causing ZeroDivisionError)
print("\nScenario 2:")
divide_numbers(10, 0)

# Scenario 3: No exception raised
print("\nScenario 3:")
divide_numbers(10, 5)
