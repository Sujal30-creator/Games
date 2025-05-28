import random
from games.words import words
import string

def get_valid_word(words):
    word=random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word=get_valid_word(words)
    word_letters= set(word) #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters=set() #What the user has guessed

    lives = 7

    #getting user input
    while len(word_letters)>0 and lives>0:
        #letters used
        print('You have',lives,'lives left and you have used these words: ',' '.join(used_letters))

        #what currenrt word is (i.e. W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters: 
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives=lives-1
                print('User letters not in the word')

        elif user_letter in used_letters:
            print('You have already used that character. Please try again')

        else:
            print('Invalid character. Please try again')

    #gets here when len(word_letters) = 0 OR when lives = 0
    if lives == 0:
        print('You died, R.I.P, The word was ',word)
    else:
        print('You guessed the word right the word was ',word,'!!')


if __name__=='__main__':
    hangman()

