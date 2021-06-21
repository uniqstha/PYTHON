# Write a program that asks the user for a number in the range of 1 to 7.
# The program should display the corresponding day of the week,
# where 1=sunday, 2=monday,3=tuesday,4=wednesday,5=thursday,6=friday,7=saturday.
# The program should display an error message if the user enters a number that is outside the range of 1 to 7.

n=int(input('Enter a number'))
if n==1:
    print('Sunday')
elif n==2:
    print('Monday')
elif n==3:
    print('Tuesday')
elif n==4:
    print('Wednesday')
elif n==5:
    print('Thursday')
elif n==6:
    print('Friday')
elif n==7:
    print('Saturday')
else:
    print('Invalid number')


