# WAP which accepts marks of four subjects and display total marks, percentage and
grade.

a=int(input('Enter the marks of first subject'))
b=int(input('Enter the marks of second subject'))
c=int(input('Enter the marks of third subject'))
d=int(input('Enter the marks of fourth subject'))
t= a+b+c+d
print(f'Total marks is {t}')
p=(t/400)*100
print(f'The total percentage is  {p}')
if p<100 and p>= 80:
    print ('Grade A')
elif p<80 and p>= 60:
    print ('Grade B')
elif p<60 and p>=40:
    print('Grade C')
else:
    print (Fail)
