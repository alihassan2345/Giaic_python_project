import random

def guess_my_number():
    computer_number = random.randint(1, 100)
    user_guess = int(input('Guess a number between 1 and 100: '))
    while computer_number != user_guess:
        if user_guess < computer_number:
            print('Too low! Try again.')
           
        else:
            print('Too high! Try again.')
        print()
        user_guess = int(input('Guess a number between 1 and 100: '))
    
    print(f'Congratulations! You guessed the number! {computer_number}')
        
guess_my_number()