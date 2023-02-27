import random
import string
from lives import lives_visual_dict

class Hangman:
    def __init__(self, word_list, num_lives=6):

        self.word = random.choice(word_list)
        self.word_guessed = "_" * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_letters = []
        self.word_list = word_list
        self.num_lives = num_lives
        self.word_guessed_list = list(self.word_guessed)

        print(f'The mystery word has {len(self.word)} characters and you have 6 lives.')
        print(*self.word_guessed, '''
        ''')

    def check_letter(self, letter):
        if letter in self.word:
            self.num_letters -= 1
            for number, placeholder in enumerate(self.word):
                if letter == placeholder:
                    self.word_guessed_list[number] = placeholder
            if self.num_lives != 1:
                print(f'You are correct! You still have {self.num_lives} lives left.')
            else:
                print(f'You are correct! You still have {self.num_lives} life left.')
            print(lives_visual_dict[self.num_lives])
            print('Letters guessed so far:', *self.list_letters)
            print(" ".join(self.word_guessed_list))
            print('\n')
        else:
            self.num_lives -= 1
            if self.num_lives != 1:
                print(f'Incorrect! You now have {self.num_lives} lives.') 
            else:
                print(f'Incorrect! You now have {self.num_lives} life.') 
            print(lives_visual_dict[self.num_lives])
            print('Letters guessed so far:', *self.list_letters)
            print(*self.word_guessed_list)
            print('\n')

    def ask_letter(self):
        alphabet = set(string.ascii_lowercase)
        while True:
            letter = input('Enter a letter: ').lower()
            if len(letter) != 1:
                print(f'You entered "{letter}". Make sure to only enter one letter.')
            elif not letter in alphabet:
                print(f'The character {letter} is not in the alphabet, please enter a letter.')     
            elif letter in self.list_letters:
                print(f'The letter "{letter}" has already been tried!')
                print('Letters guessed so far:', *self.list_letters)
                print('\n')            
            else:
                print(f'You entered "{letter}"')
                self.list_letters.append(letter)
                self.check_letter(letter)
                break

def play_game(word_list):
    game = Hangman(word_list, num_lives=6)
    while True:
        if game.num_letters == 0:
            print("Congratulations, you won!")
            print('\n')
            play_again()
            break
        elif game.num_lives == 0:
            print(f'You ran out of lives. The word was {game.word}!')
            print('\n')
            play_again()
            break
        else:
            game.ask_letter()

def play_again():
    while True:
        ask_user_to_play_again = input('Play again? Input Y or N: ').upper()
        if ask_user_to_play_again == 'Y':
            print('\n')
            print('Let\'s jump back in!')
            print('_______________________________________________________')
            print('\n')
            play_game(word_list)
            break
        elif ask_user_to_play_again == 'N':
            print('\n')
            print('Thanks for playing.')
            print('\n')
            break
        else: 
            print('Invalid selection, please choose either Y or N')

if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon', 'coconut', 'melon', 'dragonfruit']
    play_game(word_list)