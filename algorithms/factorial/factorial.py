"""
Algorithm to find factorial of a number.
Factorial of a positive integer is the product of integers from 1 to n.
The first function uses a loop to get the product, while the second function
uses recursion.
"""
def factorial(num):
    if num == 0:
        return 1
    else:
        product = 1
        for i in range(1, num+1):
            product *= i
        return product

def factorial_recursive(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num -1)
