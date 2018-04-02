# Programming-Scripting-Exercises #

Weekly exercises to be uploaded to Github to demonstrate understanding of the module.

## Week 1 Exercise ##

In this exercise, an example of a pyhton program was provided by the lecturer, Dr. Ian Mcloughlin ![Dr Ian Mcloughlin](lecturer.jpg)from [Github](https://github.com/ianmcloughlin/python-fib/blob/master/fib.py).
The python program calculated the fibonacci number when the first and last letter of the student first name is addedd together, and this number is passed through the program.  In the video lectures, the example program calculated the 30th Fibonacci number. The program  calculates the nth Fibonacci number where n the sum of the first and last letters of your first name as numbers.Using the following rule, take A as the number 1, B as 2, C as 3, and so on. Once the fibonacci number is calculated, the answer was posted to the Discussion forum.  The following was the text posted to the discussion forum: "My name is Darren, so the first and last letter of my name (D + N = 4 + 14) give the number  18. The 18th Fibonacci number is 2584".

## Week 2 Exercise ##


Here is a [link](https://github.com/ianmcloughlin/python-fib/blob/master/fibname.py) to a program that follows the exercise that was carried out in Week 1. This program works similarly to last week's exercise. Copy and run the program. Change the string variable to contain your own surname, and rerun it. Using google, investigate the ord() function.  Post the output of the program, along with any insight you have as to what ord() does, to the discussions forum.

The following was the text posted to the discussion forum:

So in my example I ran with 3 scenarios:

1.    My surname is Young (Capital Y)
2.    My surname is young (all lowercase) 
3.    My surname is YOUNG (All CAPS)

It can be seen from the program that ord () function will look at the first and last letter and return an integer/whole number from the Unicode code point.

*Scenario 1*

My surname is Young.
Programming-Scripting-Exercises/euler-5-overview.pdf The first letter Y is number 89.
The last letter g is number 103.
Fibonacci number 192 is 5972304273877744135569338397692020533504

*Scenario 2*

My surname is young.
The first letter y is number 121.
The last letter g is number 103.
Fibonacci number 224 is 29090180355503362256910111038089984964854261893.

*Scenario 3*

My surname is YOUNG
The first letter Y is number 89.
The last letter G is number 71.
Fibonacci number 160 is 1226132595394188293000174702095995.

So it can be seen that by changing the first and letter between lower case and uppercase, the ord function will return different numbers from the Unicode system. This in turn results in three different Fibonacci numbers.

What is the ord function?
Given a string of length one, return an integer representing the Unicode code point of the character when the argument is a unicode object, or the value of the byte when the argument is an 8-bit string. For example, ord('a') returns the integer 97, ord('€') (Euro sign) returns 8364.

What is Unicode? 
Unicode is a computing industry standard for the consistent encoding, representation, and handling of text expressed in most of the world's writing systems. The latest version contains a repertoire of 136,755 characters covering 139 modern and historic scripts, as well as multiple symbol sets [link to wikipedia](https://en.wikipedia.org/wiki/Unicode)

## Week 3 Exercise ##

For this exercise, after studying videos and additional information about the [collatz conjecture](https://en.wikipedia.org/wiki/Collatz_conjecture), the student is instructed to write  a single Python script that starts with an integer and repeatedly applies the Collatz function (divide by 2 if even, multiply by three and 1 if odd) using a while loop and if statement. At each iteration, the current value of the integer should be printed to the screen. The integer used was 17. The program asks for an integer at the start of the code. A very helpful book that the student found through the [Python Software Foundation](https://www.python.org/) was [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/chapter2/) with Chapter 2 giving clear explanation to both While and If statements. The source code was modified from [Stackoverflow]( https://stackoverflow.com/questions/13366830/collatz-conjecture-sequence)

## Week 4 Exercise - No exercise for this week ##

## Week 5 - Exercise 4 Euler Problem No. 5 ##

This exercise is bout writing a Python program using for and range functions to calculate the the smallest positive number that is evenly divisible by all of the numbers from 1 to 20.  It is problem 5 from [Project Euler](https://projecteuler.net/problem=5). This exercise was difficult in the sense that the problem had to be understood mathematically in order to write the pyhton program. Here is a [document](Programming-Scripting-Exercises/Euler5.pdf) that explains lowest common multiples, and an example of an algorithm for this topic.

## Week 6 Exercise ##

Write a Python script that reads the Iris data set in and prints the four numerical values on each row in a nice format. That is, on the screen should be printed the petal length, petal width, sepal length and sepal width, and these values should have the decimal places aligned, with a space between the columns.

## Week 7 Exercise ##

Write a Python script containing a function called factorial() that takes a single input/argument which is a positive integer and returns its factorial. The factorial of a number is that number multiplied by all of the positive numbers less than it. For example, the factorial of 5 is 5x4x3x2x1 which equals 120. In the script, test the function by calling it with the values 5, 7, and 10.
