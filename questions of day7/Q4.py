#Write a python program to print factorial of a given number?

def factorial(num):
    product=1
    for i in range (2, num+1):
        product=product*i
    return product
print (factorial(5))