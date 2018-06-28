from random import randint

print('Hello! What is your name?')
myName = input()

number = randint(1, 20)
print ('Well, {}, I am thinking of a number between 1 and 20'.format(myName))

guess_num = 1
while guess_num < 7:
    print('Take a guess.')
    guess = int(input())
    if guess < number:
        print('Your guess is too low.')
        guess_num += 1
    elif guess > number:
        print('Your guess is too high.')
        guess_num += 1
    elif guess == number:
        break
else:
    print('Nope. The number I was thinking of was {}'.format(number))

if guess == number:
    print('Good job, {0}! You guessed my number in {1} guess{2}!'.format(
        myName, guess_num, '' if guess_num == 1 else 'es'))
