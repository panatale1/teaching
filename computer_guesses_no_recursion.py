print("Pick a number between 1 and 1,000,000")
raw_input("Hit Enter when you have it")
low = 1
high = 1000000
while low < high:
    mid = (high + low) / 2
    response = raw_input("Is your number {}?(yes/no) ".format(mid))
    if response.lower()[0] == 'y':
        break
    response = raw_input("Is your number larger than {}?(yes/no) ".format(mid))
    if response.lower()[0] == 'y':
        low = mid + 1
    else:
        high = mid - 1

print("Your number is: {}".format(low if low == high else mid))
