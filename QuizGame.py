yes_strings = ['y', 'Y', 'yes', 'Yes']

print('Welcome to the quiz!')

playing = input('Do you want to play? ')

if playing not in yes_strings:
    print('No Play')
    quit()
else:
    print('Yes Play ')

print('Lets play!')

user_answer = input('1. What does CPU stand for? ')
q1_answer = ('central processing unit', 'Central Processing Unit')
if user_answer in q1_answer:
    print('Congrats! Question 1 response is correct!')
else:
    print('Sorry, Question 1 response is incorrect.')