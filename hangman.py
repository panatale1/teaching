from random import sample
from string import ascii_lowercase

HANGMAN_PICS = ['''
    +---+
        |
        |
        |
       ===''', '''
    +---+
    O   |
        |
        |
       ===''', '''
    +---+
    O   |
    |   |
        |
       ===''', '''
    +---+
    O   |
   /|   |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
       ===''']

words = {
    'Animals': '''ant baboon badger bat bear beaver camel cat clam cobra cougar
 coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk
 lion lizard llama mole monkey moose mouse mule newt otter owl panda
 parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep
 skunk sloth snake spider stork swan tiger toad trout turkey turtle
 weasel whale wolf wombat zebra'''.split(),
    'Colors': 'red orange yellow green blue indigo violet teal aqua peach brown black white grey'.split(),
    'Shapes': '''square circle hexagon rectangle pentagon octagon triangle
 cube sphere cylinder pyramid tetrahedron prism ellipse rhombus trapezoid chevron'''.split(),
    'Fruits': '''apple orange lemon lime pear watermelon grape grapefruit cherry
 banana cantaloupe mango strawberry tomato pineapple tangerine apricot peach'''.split()
}

def get_random_word(word_dict):
    print('Would you like a random category?')
    if raw_input().lower().startswith('y'):
        category = sample(word_dict.keys(), 1)[0]
        print('Your random category is: {}'.format(category))
        return sample(word_dict[category], 1)[0]
    else:
        print('Your categories are: {}'.format(sorted(word_dict.keys())))
        category = raw_input().title()
        print('You have selected {}.'.format(category))
        return sample(word_dict[category], 1)[0]

def found_all_letters(secret_word, correct_letters):
    for letter in secret_word:
        if letter not in correct_letters:
            return False
    else:
        return True

def play_again():
    print('Would you like to play again? (yes or no)')
    return raw_input().lower().startswith('y')

def get_guess(already_guessed):
    while True:
        print('Guess a letter.')
        guess = raw_input().lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in already_guessed:
            print('You have already guessed that letter. Choose again')
        elif guess not in ascii_lowercase:
            print('Please enter a LETTER.')
        else:
            return guess

def display_board(missed_letters, correct_letters, secret_word, blanks):
    print(HANGMAN_PICS[len(missed_letters)])
    print('\n')
    print('Missed letters: ')
    print(' '.join(missed_letters))
    print('\n')
    print(' '.join(blanks))
    print('\n')


print('H A N G M A N')
missed_letters = []
correct_letters = []
secret_word = get_random_word(words)
blanks = ['_' for i in secret_word]
game_is_done = False
finished = False

while not finished:
    display_board(missed_letters, correct_letters, secret_word, blanks)
    guess = get_guess(missed_letters + correct_letters)
    if guess in secret_word:
        correct_letters.append(guess)
        index = -1
        for i in range(secret_word.count(guess)):
            index = secret_word.index(guess, index + 1)
            blanks[index] = guess
        if found_all_letters(secret_word, correct_letters):
            print('Yes! The secret word is "' + secret_word + '"! You win!')
            game_is_done = True
    else:
        missed_letters.append(guess)
        if len(missed_letters) == 6:
            display_board(missed_letters, correct_letters, secret_word, blanks)
            print('Sorry, you\'ve run out of guesses! The word was "' + secret_word + '"')
            game_is_done = True
    if game_is_done:
        if play_again():
            missed_letters = []
            correct_letters = []
            secret_word = get_random_word(words)
            blanks = ['_' for i in secret_word]
            game_is_done = False
        else:
            finished = True
