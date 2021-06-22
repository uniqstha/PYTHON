# A students take B apples and distribute them among each other evenly.
# The remaining (the undivisible) part remains in the basket. How many apples will each single student get?
# How many apples will remain in the basket? The program reads the numbers A and B.
# It should print the two answers for the questions above.

A=int(input('Enter the number of students: '))
B=int(input('Enter the number of apples: '))
C=B//A
d=B%A
print(f'Each single students gets {C} apples')
print(f'{d} apples remains in the basket')