# https://www.youtube.com/watch?v=JwO_25S_eWE from Khan Academy Definining a factorial function
# ttps://stackoverflow.com/questions/26499776/python-using-def-in-a-factorial-program

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
