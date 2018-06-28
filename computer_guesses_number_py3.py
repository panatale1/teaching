def guess_number(low, high):
    if low == high:
        return low
    mid = int((high + low) / 2)
    response = input("Is your number {}?(yes/no) ".format(mid))
    if response.lower()[0] == 'y':
        return mid
    response = input("Is your number larger than {}?(yes/no) ".format(mid))
    if response.lower()[0] == 'y':
        return guess_number(mid+1, high)
    return guess_number(low, mid-1)


print("Pick a number between 1 and 1,000,000")
input("Hit Enter when you have it")
print("Your number is: {}".format(guess_number(1, 1000000)))
