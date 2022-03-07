import random
draw = 0
won = 0
lost = 0
while True:
    userChoice = input('Enter your choice:  rock, paper, scissor ')
    computerChoice = random.choice(['rock', 'paper', 'scissor'])
    print()
    if userChoice == computerChoice:
        print('DRAW!')
        draw+=1
    elif computerChoice == 'rock':
        if userChoice == 'paper':
            print('YOU WON!🏆  Paper Beats Rock')
            won+=1
        else:
            print('YOU LOSE!  Rock Beats Scissor')
            lost+=1
    elif computerChoice == 'paper':
        if userChoice == 'scissor':
            print('YOU WON!🏆  Scissor Beats paper')
            won+=1
        else:
            print('YOU LOSE!   Paper Beats Rock')
            lost+=1
    elif computerChoice == 'scissor':
        if userChoice == 'rock':
            print('YOU WON!  Rock Beats Scissor')
            won+=1
        else:
            print('YOU LOSE! Scissor Beats Paper')
            lost+=1
    else:
        print('Please enter valid input')
    
    print()
    print('Won =', won,  'Lost =', lost,  'Draw =', draw)
    print()


