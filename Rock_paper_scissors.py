from random import choice

def play():
    user = input("What's your choice?\n 'r' for rock, 'p' for paper and 's' for scissors\n")
    computer = choice(['r','p','s'])

    if user == computer:
        return 'It\'s a tie'
    
    if is_win(user,computer):
        return 'You win!'
    
    return 'You lost!'

def is_win(player,opponent):
    #return true if player wins
    #p>r,s>p,r>s
    if (player == 'r' and opponent == 's') or (player=='s' and opponent == 'p')\
    or (player =='p' and opponent=='r'):
        return True
    
print(play())