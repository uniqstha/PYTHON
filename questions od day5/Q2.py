# Write a program that asks the user for a number in the range of 1 to 12.
# The program should display the corresponding month,
# where 1=january, 2=february,3=march,4=april,5=may,6=june,7=july, 8=august,9=september,
# 10=october,11=november,12=december. The program should display an error message if the user enters a number
# that is outside the range of 1 to 12.



i = int(input('Enter a number from 1-12: '))

if i==1:
    print('January')
elif i==2:
    print('Feburary')
elif i==3:
    print('March')
elif i==4:
    print('April')
elif i==5:
    print('May')
elif i==6:
    print('June')
elif i==7:
    print('July')
elif i==8:
    print('August')
elif i==9:
    print('September')
elif i==10:
    print('October')
elif i==11:
    print('November')
elif i==12:
    print('December')
else:
    print("Invalid number")

