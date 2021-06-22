#Given a three-digit number. Find the sum of its digits.


number = int(input('Enter a thre digit integer: '))
a = number // 100
b = number // 10 % 10
c = number % 10
d=a+b+c
print(f'The sum of digits is {d}')

