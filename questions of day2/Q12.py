# A school decided to replace the desks in three classrooms. Each desk sits two students.
#Given the number of students in each class, print the smallest possible number of desks that can be purchased.
#The program should read three integers: the number of students in each of the three
#classes, a, b and c respectively.



G1=int(input("enter the number of student in first class :"))
G2=int(input("enter the number of students in second class :"))
G3=int(input("enter the number of students in third class:"))
D1=(G1//2)
print(f"the required number of desk for first class is {D1}")
D2=(G2//2)
print(f"the required number of desks for second class is {D2}")
D3=(G3//2)
print(f"the required number of desks for third class is {D3}")
R1=(G1%2)
print(f"remaining desk for first class is {R1} ")
R2=(G2%2)
print(f"remaining desk for second class is {R2} ")
R3=(G3%2)
print(f"remaining desk for third class is {R3} ")
T=D1+D2+D3+R1+R2+R3
print(f"total number of desks that can be purchased is {T} ")