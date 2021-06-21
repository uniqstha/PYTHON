#Write a program to convert second into hour, minute & second.


sec = int(input('Enter seconds: '))
hr = sec // 3600
sec %= 3600
min = sec // 60
sec %= 60
sec = sec % (24 * 3600)

print(f'{hr} hours and {min} minutes and {sec} seconds')
