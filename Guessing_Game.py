#This is the guess game
import random
print('What is your naame?')
name = input()
secretNumber = random.randint(1,20)
print('Hello! '+ name +' , I am thinking of a number between 1 and 20.')


#Ask user for 6 times
for takeguess in range(1,7):
    print('Take a guess')
    guess = int(input())
    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break #This is the correct guess

if guess == secretNumber:
    print('Good job, '+ name +'! You guessed my number in '+ str(takeguess) + ' guesses')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))
        

