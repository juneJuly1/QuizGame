yes_strings = ['y', 'Y', 'yes', 'Yes']



print('Welcome to the quiz!')

playing = input('Do you want to play? ')

if playing not in yes_strings:
    print('No Play')
    quit()
else:
    print('Yes Play')

