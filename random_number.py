import random
import time


def guess(x):
    random_number = random.randint(1,10)
    guess=0
    start_time = time.time()                                     
    while guess != random_number:
        guess = int(input(f'Guess a random number between 1 and {x}: '))
        if guess< random_number:
            print("Sorry,guess again, Too Low.")
        elif guess>random_number:
            print("Sorry,Guess again. Too high")
    
    time_taken= round((time.time()-start_time),2)
    print("You guessed it in " + str(time_taken) + ".")

guess(10)
#IF we want computer to guess it 

def computer_guess(x):
    low=1
    high=x
    feedback=''
    while feedback != 'c':
        if low!=high:
            guess = random.randint(low,high)
        else:
            guess = low #could also be high b/c low = high
        
        feedback= input(f'Is {guess} too high (H), too low (L) or correct (C)')
        if feedback == 'h':
            high = guess-1
        elif feedback=='l':
            low = guess+1

    print(f'Yay! The computer guessed you number, {guess}, correctly!')

#computer_guess(100)
#Uncooment above to run the computer guessing function

        