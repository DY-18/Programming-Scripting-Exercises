#Darren Young, 2018-2-11
# Week 3 GMIT The Collatz Conjecture 
# source code: modified from  https://stackoverflow.com/questions/13366830/collatz-conjecture-sequence

n = int(input("Please enter an integer:"))

while n > 1:
        if n % 2 == 0 :
            n = n // 2
            print(n)
        elif n % 2 == 1 :
            n = 3 * n + 1
            print(n)
        if n == 1 :
            break
