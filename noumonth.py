# Guess the number and get the month of the year

# create a tuple
month = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
         'December')

while True:
    x = int(input('Enter the number from 1 - 12 : '))
    if x == 0:
        print('End of the game better luck next time...!')
        break
    if x > 12 or x < 1:
        print('Invalid number, enter number from 1 - 12')
    else:
        print(month[x-1])

