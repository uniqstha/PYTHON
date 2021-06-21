#Given the integer N - the number of minutes that is passed since midnight -
# how many hours and minutes are displayed on the 24h digital clock?

N=int(input('Enter the no. of minutes that passed since midnight'))
hr= N//60
min=N%60
print(f'{hr} hours and {min} minutes is displayed in the 24 hr clock')