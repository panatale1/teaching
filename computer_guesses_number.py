def guess_number(low, high):
    if low == high:
        return low
    mid = (high + low) / 2
    response = raw_input("Is your number {}?(yes/no) ".format(mid))
    if response.lower()[0] == 'y':
        return mid
    response = raw_input("Is your number larger than {}?(yes/no) ".format(mid))
    if response.lower()[0] == 'y':
        return guess_number(mid+1, high)
    return guess_number(low, mid-1)


print("Pick a number between 1 and 1,000,000")
raw_input("Hit Enter when you have it")
print("Your number is: {}".format(guess_number(1, 1000000)))
