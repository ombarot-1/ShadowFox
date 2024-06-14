import random

words_with_hints = [
    {"word": "python", "hint": "A popular programming language"},
    {"word": "hangman", "hint": "The name of this game"},
    {"word": "cybersecurity", "hint": "Protection of computer systems from theft"},
    {"word": "forensics", "hint": "Scientific tests to detect crimes"},
    {"word": "encryption", "hint": "Process of converting information into code"},
]

hangman_visual = [
    """
     -----
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]

def get_word():
    return random.choice(words_with_hints)

def get_visual(tries):
    print(hangman_visual[tries])

def display_word(word, guessed_letters):
    display = "".join([letter if letter in guessed_letters else '_' for letter in word])
    print(f'Word: {display}')

word_info = get_word()
word = word_info['word']
hint = word_info['hint']
guessed_letters = set()
wrong_guess = 0
max_guess = len(hangman_visual) - 1

print('-: Welcome to Hangman Game :-')
print(f'Hint: {hint}')

while wrong_guess < max_guess:
    get_visual(wrong_guess)
    display_word(word, guessed_letters)

    guess = input('Enter your letter: ').lower()

    if len(guess) != 1 or not guess.isalpha():
        print('Please enter a single letter.')
        continue

    if guess in guessed_letters:
        print('Letter was previously entered.')
    
    elif guess in word:
        guessed_letters.add(guess)
        print('Your guess is correct.')
    
    else:
        wrong_guess += 1
        print('Your guess is not correct.')

    if all(letter in guessed_letters for letter in word):
        print("Congratulations! You've guessed the word correctly!")
        display_word(word, guessed_letters)
        break
else:
    get_visual(wrong_guess)
    print('Oops! You lost the game.')
    print(f'The word was: {word}')
