import random

# List of words to guess
words = ['python', 'computer', 'game', 'music', 'book', 'movie', 'friend', 'family', 'school', 'happy']

# Hangman drawings
hangman_pics = [
    '''
    +---+
    |   |
        |
        |
        |
        |
  =========''',
    '''
    +---+
    |   |
    O   |
        |
        |
        |
  =========''',
    '''
    +---+
    |   |
    O   |
    |   |
        |
        |
  =========''',
    '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
  =========''',
    '''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
  =========''',
    '''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
  =========''',
    '''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
  ========='''
]

def play_game():
    # Pick a random word
    word = random.choice(words)
    
    # Keep track of guessed letters
    guessed_letters = []
    wrong_guesses = 0
    
    print("Welcome to Hangman!")
    print("Try to guess the word!")
    
    # Keep playing until win or lose
    while True:
        # Show hangman picture
        print(hangman_pics[wrong_guesses])
        
        # Show the word with blanks
        word_display = ""
        for letter in word:
            if letter in guessed_letters:
                word_display += letter + " "
            else:
                word_display += "_ "
        
        print("Word:", word_display)
        print("Guessed letters:", guessed_letters)
        print("Wrong guesses:", wrong_guesses, "out of 6")
        
        # Check if player won
        if all(letter in guessed_letters for letter in word):
            print("You won! The word was:", word)
            break
        
        # Check if player lost
        if wrong_guesses >= 6:
            print("You lost! The word was:", word)
            break
        
        # Get player's guess
        guess = input("Guess a letter: ").lower()
        
        # Check if already guessed
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
        
        # Add to guessed letters
        guessed_letters.append(guess)
        
        # Check if guess is in the word
        if guess in word:
            print("Good guess!")
        else:
            print("Wrong guess!")
            wrong_guesses += 1
        
        print("-" * 30)

# Start the game
while True:
    play_game()
    
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes" and play_again != "y":
        print("Thanks for playing!")
        break