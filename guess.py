from random import randint

print "Hello! What is your name?"
my_name = raw_input()

number = randint(1, 20)
print "Well, {}, I am thinking of a number between 1 and 20".format(my_name)

guess_num = 1
while guess_num < 7:
    guess = int(raw_input('Take a guess: '))
    if guess < number:
        print 'Your guess is too low.'
        guess_num += 1
    elif guess > number:
        print 'Your guess is too high.'
        guess_num += 1
    else:
        break

if guess == number:
    if guess_num == 1:
        print 'Good job, {0}! You guessed my number in {1} guess!'.format(
            my_name, guess_num
        )
    else:
        print 'Good job, {0}! You guessed my number in {1} guesses!'.format(
            my_name, guess_num
        )
else:
    print "Nope. The number I was thinking of was {}".format(number)
