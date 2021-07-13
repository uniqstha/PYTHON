def palin():
    a=input('Enter a sting: ')
    b= a[::-1]
    if a==b:
        print('The given string is palindrome')
    else:
        print('The given string is not palindrome')
palin()