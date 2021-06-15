#3. N students take K apples and distribute them among each other evenly. The remaining
# (the undivisible) part remains in the basket. How many apples will each single student get?
# How many apples will remain in the basket? The program reads the numbers N and K.
# It should print the two answers for the questions above.

N=int(input("No of students : "))
K= int(input('Total no of apples'))
a= K//N
b= K%N
print(f'Each student gets {a} apples')
print(f'{b} apple remains in the basket')