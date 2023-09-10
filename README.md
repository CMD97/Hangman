# Hangman Project for AICore
The Hangman Project created was using Python3 & VSCode, this is the initial project I have created to begin understanding the use of several Python basics, inclusive of classes, functions, loops, sets, lists, booleans & user inputs. The hangman game can be accessed via the command line by accessing the folder and inputting `python hangman.py`. The game was created by following the milestones as detailed below.

## Milestone 1: Setting up the environment.
I began by understanding how to set up the environment by installing miniconda & pip and creating the environment that will launch upon opening the hangman.py file inside VSCode.

The next step was to be able to understand how git commands, and begin using the commands within the command line to be able to clone github files, be able to stage, commit & push changes as well as linking a repository to a folder that contains the local files.

## Milestone 2: Creating variables for the game

Within this milestone I utilised python's in-built list function to be able to create a word list for the game to choose from. My current list is shown here:
`word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon', 'coconut', 'melon', 'dragonfruit']`

In Hangman the word has to be chosen at random, to do this I used the in-built random function firstly by using `import random`, then making the word chosen equal to a random choice from the list. e.g. `self.word random.choice(word_list)`.

Hangman also allows the user to input a letter to be able to start guessing the word, I used the in-built input() function to be able to prompt the user to enter a letter by stating `input("Enter a letter: ").lower`. THe addition of the .lower ensured that if the user entered an uppercase letter, it would be returned as a lowercase, as my word list is in lowercase, and python would define an uppercase letter differently to a lowercase letter.

The input function needed to have conditionals so the user wouldn't be able to type anything for their input. I utilised an if/elif/else statement to ensure they had a good experience, with prompts to try again if they entered something incorrect. This was all inputted into an ask_letter method within the Hangman class, inside a loop until the letter passed through to the else statement:

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
len() was used to ensure the user only entered 1 letter, if the letter was not within the English language, a message stating it wasn't would be printed, if the letter had been tried a message would be printed, then if they entered a valid letter they haven't used, it would go toward the check_letter function. 

## Milestone 3: First steps in the check_letter method.
After the letter is passed through the if/elif/else statement provided in Milestone 2, it moves onto the next method to be able to check if the letter is in the word. This was done by creating another if/else statement, if the letter is in the word the code will print: `print(f'You are correct! You still have {self.num_lives} lives left.')` and if it is not in the word it will print: `print(f'Incorrect! You now have {self.num_lives} lives.') `.

## Milestone 4: Class creation & further check_letter method requirements.

A class was created named 'Hangman' which included the method ask_letter() and check_letter(), as well as the magic method of \_\_init\_\_ which was learnt to be able to initialise upon running the code noted below:

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
The attributes above assisted to define the parameters for the hangman game.

Next was to complete the check_letter() method to be able to ensure that when the user inputs a letter, it iterates through the list of blank spaces and replaces it with the letter at the specific point, for this I began to understand the use of a for loop and the enumerate function, along with turning the string of the word into a list so that each letter had a position due to the index.

    if letter in self.word:
            self.num_letters -= 1
            for number, placeholder in enumerate(self.word):
                if letter == placeholder:
                    self.word_guessed_list[number] = placeholder
This function used a boolean to see if the letter was in the word, and if it was it would replace the blank space with the letter at the correct position e.g. if 'a' was inputted, the blank spaces would turn from "\_ \_ \_ \_ \_" to "a \_ \_ \_ \_". 

As per the if statement, once the letter has passed the check that it is in the word, it will also reduce the number of unique numbers by 1, this variable was created in the \_\_init\_\_ method and is the main attribute to determine if the game is won.

To continue from the if statement started above, an else block was created in case the letter is not in the word.

    else:
            self.num_lives -= 1
 This deducted from the lives of 6 that I used for the game, this will determine if the user has lost the game.
 
## Milestone 5: Putting the methods to use within the play_game function.
The final step was to create the `play_game()` function, which would then be called upon to be able to run through the class 'Hangman':
    
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
The while loop was created within the play_game function to call upon the ask_letter method within the class as long as the number of unique letters wasn't equal to zero (insinuating the user has won) and the number of lives wasn't equal to zero (insinuating the user has lost), if the if or elif statements were brought into control, the game ended with the specific print statements above.

## Milestone 6: Additional details added.
To take the game further, the visual of hangman was added by a separate file, called `lives.py` within the file was a dicttionary which printed the visual allocated to the key called `lives_visual_dict`. This was imported at the beginning of the file by line 4: `from lives import lives_visual_dict` and was called upon in the check_letter method after both the letters were correct, or the letters were incorrect so that there was a better user experience.

Finally, I created a function that asked the user if they wanted to play again, so the user didn't have to restart the code at the end. This was an additional detail outside of the project that I thought would complete the user experience & give them a reason to stay for another game and is coded into the play_game function underneath the if/elif statements.

    ef play_again():
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
As shown, it has a while loop with an if/elif/else statement to ensure the conditionals are met if the user inputs anything other than Y or N and the input is taken to .upper() so that if the user inputs a lowercase y or n the code will take that into an uppercase letter and not throw an error toward them. The function will then circle back round to the initial play_game function if they select Y, or end the code if they select N. Any other character returns an invalid selection and will ask them to choose either Y or N once again.

## Conclusion
Throughout this project, I have successfully understood the basics of Python & fortified the more complex parts by creating a final function as an addition to the project that wasn't necessary, the play_again function, which is inclusive of a while loop, and also an if/elif/else statement. 
What I did find to be a struggle was understanding the enuemrate function, which I will be going over to be able to understand more and have been doing so since gaining the basics of how it works within the for loop.

The next things I'd add to improve my version of hangman is to create a difficulty setting, however I didn't implement this in it's current state due to it being subjective; is the difficulty the amount of letters, unique letters or number of lives given. I am confident with a bit of time I would be able to code this in at a later date.