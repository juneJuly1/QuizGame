# Welcoming user and getting user input.
print('Welcome to the quiz!')

playing = input('Do you want to play? ')

# Checking if user wants to play.
yes_strings = ['y', 'yes']

if playing.lower() not in yes_strings:
    print('No Play')
    quit()
else:
    print('Yes Play ')

print('Lets play!')

score = 0

# Question 1
user_answer = input('1. What does CPU stand for? ')
q_answer = 'central processing unit'
if user_answer.lower() in q_answer:
    print('Correct!')
    score += 1
else:
    print('Incorrect.')

# Question 2
user_answer = input('2. What does GPU stand for? ')
q_answer = 'graphics processing unit'
if user_answer.lower() in q_answer:
    print('Correct!')
    score += 1
else:
    print('Incorrect.')

# Question 3
user_answer = input('3. What does PSU stand for? ')
q_answer = 'power supply unit'
if user_answer.lower() in q_answer:
    print('Correct!')
    score += 1
else:
    print('Incorrect.')

print('You got ' + str(score) + '/3 questions correct.')
print('You got ' + str(score/3) * 100 + '%')