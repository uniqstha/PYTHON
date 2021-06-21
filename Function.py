def add():
    a=int(input('a: '))
    b= int(input('b: '))
    c=a+b
    print(f'The sum is {c}')
add()

def sub():
    a = int(input('a: '))
    b = int(input('b: '))
    c = a - b
    return c
sub()
print(f'The sub is{sub()}')

def mul(a,b):
    c=a*b
    print(f'The multiplication is {c}')
mul(5,3)

def div(a,b):
    c=a/b
    return c

a=int(input("a:"))
b= int(input("b:"))

ans=div(a,b)
print(ans)
