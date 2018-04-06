# Modified from original code Sarah Scholz 04/03/2018
# Function to find factorial of a given number

def factorial(x):  # Define a function and passing a parameter

    n = 1          # Declare a variable fact and set the initial value=1

    for i in range (1, x + 1):  # Using loop for iteration

        n = i * n

    return n

print("The factorial of 5 is", factorial(5))

print("The factorial of 7 is", factorial(7))

print("The factorial of 10 is", factorial(10))
