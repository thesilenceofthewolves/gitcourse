import random

def play(x):
    random_nummber = random.randint(1, x)
    player_guess = 0
    tries = 3
    #player_guess = input(f"Guess a number between 1 and {x}  ")
    

    while tries > 0 and player_guess != -1:
        player_guess = int(input(f"Guess a number between 0 and {x}:  "))
    
        if player_guess != random_nummber and player_guess != -1:
            print(" Try again !!!")
            tries -= 1
        elif player_guess == random_nummber:
            print("well done", player_guess, " is correct")
            break
    if tries == 0 and player_guess != random_nummber:
        print('Game is over !', random_nummber, ' was the correct number')

    print('See you next time')


x = random.randint(1, 200)
#play(x)
guessed_number = []
def computer_guess(x):
    secret_number = random.randint(0,x)
    #print(secret_number, 'is the secret number')
    feedback = ''
    guess = -1
    guessed = 0
    while feedback != 'c' and secret_number != guess:
        guess = random.randint(1, x)
        guessed += 1
        if guess in guessed_number:
            #print( guess, 'Already choose')
            continue 
        guessed_number.append(guess)
        '''if guess in guessed_number:
            #print( guess, 'Already choose')
            continue '''
        #feedback = input(f'Is {guess} too high (h), too low(l), corrct(c) ?')
        if guessed > 10 and secret_number != guess :
          print('Game over!!! You guessed more than 10 times!', f' Your last guess was {guess}.' f'The right number was {secret_number}')
          break

        elif guess > secret_number:
            feedback = f'{guess} is too high'
            print(feedback)
        elif guess < secret_number:
            feedback = f'{guess} is Too low'
            print(feedback)
        

   
    else:
        print(f'Yay {guess} is correct !!! It took you', f'{guessed} attempts')
    

    
    
computer_guess(x)



def main():
    while input("Play Again? (Y/N) ").upper() == "Y":
        #play(x)
        computer_guess(x)


if __name__ == "__main__":
    main()