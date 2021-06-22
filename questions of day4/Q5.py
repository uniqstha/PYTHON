#Given three integers, print the smallest one. (Three integers should be user input)

a=int(input('Enter the first number: '))
b=int(input('Enter the second number: '))
c=int(input('Enter the third number: '))
if a<b<c :
    print(f'The smallest integer is {a}')
elif b<c<a:
    print(f'The smallest integer is {b}')
else:
    print(f'The smallest integer is {c}')
