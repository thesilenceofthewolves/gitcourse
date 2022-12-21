from random import randint
import random

account = int(input("How much money do you have?"))
while account > 0:
    play=int(input("if you wnat you play press 1 if not press 0"))
    if play == 0:
        print("Bye !")
        break
    else:
        print("lets go")
    bet = int(input("How much do you want to bet?"))
    while bet > account:
        print('You bet more than you have')
        bet = int(input("Bet what you can pay"))
    while bet <= 0:
        print(" you nned to bet a value > 0")
        bet = int(input("SO what is your bet?"))
    choice = int(input("Enter a number between 0 and 49:"))
    if choice == random.randint(0,49):
            bet *= 50
            account += bet
            print(" you won £ {} !!!" .format(bet), "you have now £{}" .format(account))
            

    else: 
        account -= bet
        print("Oups! you lost this time", "you now have £ {}" .format(account))

else: print(" you don't have enough money to bet")