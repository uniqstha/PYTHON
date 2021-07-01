#Write a Python function that takes a number as a parameter and check the number is prime or not.

num= int(input("Enter any number: "))

# prime number is always greater than 1
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(f"{num}is not a prime number")
            break
    else:
        print(f"{num} is a prime number")

# if the entered number is less than or equal to 1
# then it is not prime number
else:
    print(f"{num}is not a prime number")