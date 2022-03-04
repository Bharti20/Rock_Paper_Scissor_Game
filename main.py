import random

userChoice = input('Enter your choice:  rock, paper, scissor ')
computerChoice = random.choice(['rock', 'paper', 'scissor'])
print()
if userChoice == computerChoice:
    print('Game is draw!  because', 'computer chosen', computerChoice) 
elif computerChoice == 'rock':
    if userChoice == 'paper':
        print('You won! because', 'computer chosen', computerChoice)
    else:
        print('Computer won! because', 'computer chosen', computerChoice) 
elif computerChoice == 'paper':
    if userChoice == 'scissor':
        print('You won!  because', 'computer chosen', computerChoice) 
    else:
        print('Computer won!  because', 'computer chosen', computerChoice) 
elif computerChoice == 'scissor':
    if userChoice == 'rock':
        print('You won!  because', 'computer chosen', computerChoice) 
    else:
        print('Computer won!  because', 'computer chosen', computerChoice) 
else:
    print('Please enter valid input') 
