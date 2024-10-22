from random import randint

print('Welcome to the Number Guessing Game!')
print('\nPlease select the difficulty level:')
print('1. Easy (10 chances)')
print('2. Medium (5 chances)')
print('3. Hard (3 chances)\n')

choice = int(input("Enter your choice: "))

if choice == 1:
    chances = 10
elif choice == 2:
    chances = 5
else:
    chances = 3

print('\nGreat! You have selected the Medium difficulty level.')
print('Let\'s start the game!')

print('\nI\'m thinking of a number between 1 and 100.')
randomNumber = randint(1, 100)

print(f'You have {chances} chances to guess the correct number.')
for i in range(chances):
    guess = int(input('\nEnter your guess: '))
    if guess == randomNumber:
        print('Congratulations! You have guessed the correct number.')
        break
    elif guess < randomNumber:
        print(f'Incorrect! The number is greater than {guess}.')
    else:
        print(f'Incorrect! The number is less than {guess}.')
else:
    print('\nSorry! You have run out of chances.')
    print(f'The correct number was {randomNumber}.')