# Welcoming user and getting user input.
print('Welcome to the quiz!')

playing = input('Do you want to play? ')

# Checking if user wants to play.
yes_strings = ['y', 'Y', 'yes', 'Yes']

if playing not in yes_strings:
    print('No Play')
    quit()
else:
    print('Yes Play ')

print('Lets play!')

# Question 1
user_answer = input('1. What does CPU stand for? ')
q_answer = ('central processing unit', 'Central Processing Unit')
if user_answer in q_answer:
    print('Correct!')
else:
    print('Incorrect.')

# Question 2
user_answer = input('2. What does GPU stand for? ')
q_answer = ('graphics processing unit', 'Graphics Processing Unit')
if user_answer in q_answer:
    print('Correct!')
else:
    print('Incorrect.')

# Question 3
user_answer = input('3. What does PSU stand for? ')
q_answer = ('power supply unit', 'Power Supply Unit')
if user_answer in q_answer:
    print('Correct!')
else:
    print('Incorrect.')