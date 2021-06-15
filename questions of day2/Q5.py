#Check whether the user input number is even or odd and display it to user.

a=int(input("Enter a number"))
check=a%2
if check==0:
    print("The given number is even")
else:
    print('The given number is odd')
print ('program end')