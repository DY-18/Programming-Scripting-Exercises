### Programming-Scripting-Exercises
Weekly exercises to be uploaded
## Week 1 Exercise ##
Calcualte the fibonacci number using th first and last letter of the student first name
## Week 2 Exercise ##
So in my example I ran with 3 scenarios:
1.    My surname is Young (Capital Y)
2.    My surname is young (all lowercase)
3.    My surname is YOUNG (All CAPS)
It can be seen from the program that ord () function will look at the first and last letter and return an integer/whole number from the Unicode code point.
My surname is Young
The first letter Y is number 89
The last letter g is number 103
Fibonacci number 192 is 5972304273877744135569338397692020533504

My surname is young
The first letter y is number 121
The last letter g is number 103
Fibonacci number 224 is 29090180355503362256910111038089984964854261893

My surname is YOUNG
The first letter Y is number 89
The last letter G is number 71
Fibonacci number 160 is 1226132595394188293000174702095995
So it can be seen that by changing the first and letter between lower case and uppercase, the ord function will return different numbers from the Unicode system. This in turn results in three different Fibonacci numbers.
What is the ord function?
Given a string of length one, return an integer representing the Unicode code point of the character when the argument is a unicode object, or the value of the byte when the argument is an 8-bit string. For example, ord('a') returns the integer 97, ord('€') (Euro sign) returns 8364.

What is Unicode? 
Unicode is a computing industry standard for the consistent encoding, representation, and handling of text expressed in most of the world's writing systems. The latest version contains a repertoire of 136,755 characters covering 139 modern and historic scripts, as well as multiple symbol sets. 
## Week 3 Exercise ##
For this exercise, after studying videos and additional information about the [collatz conjecture](https://en.wikipedia.org/wiki/Collatz_conjecture), the student is instructed to write  a single Python script that starts with an integer and repeatedly applies the Collatz function (divide by 2 if even, multiply by three and 1 if odd) using a while loop and if statement. At each iteration, the current value of the integer should be printed to the screen. The integer used was 17. The program asks fir an integer at the start of the code.
## Week 5 - Exercise 4 Euler Problem No. 5 ##
This exercise is bout writing a Python program using for and range functions to calculate the the smallest positive number that is evenly divisible by all of the numbers from 1 to 20.  It is problem 5 from [Project Euler](https://projecteuler.net/problem=5). 
