# Write a program function to find max of three numbers.(no parameter and no return type)

def max():
    a=int(input('Enter first number: '))
    b= int(input('Enter second number: '))
    c= int(input('Enter third number: '))
    if a>b>c :
        print(a)
    elif b>c>a:
        print(b)
    else:
        print(c)
max()