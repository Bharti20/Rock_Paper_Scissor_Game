import random

userChoice = input('Enter your choice:  rock, paper, scissor ')
computerChoice = random.choice(['rock', 'paper', 'scissor'])
print()
if userChoice == computerChoice:
    print('DRAW!') 
elif computerChoice == 'rock':
    if userChoice == 'paper':
        print('YOU WON!  Paper Beats Rock')
    else:
        print('YOU LOSE!  Rock Beats Scissor') 
elif computerChoice == 'paper':
    if userChoice == 'scissor':
        print('YOU WON!  Scissor Beats paper') 
    else:
        print('YOU LOSE!   Paper Beats Rock') 
elif computerChoice == 'scissor':
    if userChoice == 'rock':
        print('YOU WON!  Rock Beats Scissor') 
    else:
        print('YOU LOSE! Scissor Beats Paper') 
else:
    print('Please enter valid input') 
