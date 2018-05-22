from copy import deepcopy
from random import seed, shuffle
from string import digits, letters, punctuation


SYMBOLS = digits + letters + punctuation + ' '
MAX_KEY_SIZE = len(SYMBOLS)


class CipherMachine(object):
    message = None
    key = None
    mode = None
    cipher = None
    translated = ''

    def get_cipher(self):
        while True:
            print 'Which cipher would you like to use?'
            cipher = raw_input().lower()
            if cipher in ['caesar', 'c', 'shift', 's', 'vigenere', 'v', 'substitution', 'u', 'zigzag', 'z', 'a', 'atbash']:
                self.cipher = cipher
                break
            else:
                print 'Enter either "(A)tbash, (C)aesar", "(S)hift", "S(u)bstitution", "(V)igenere", or "(Z)igzag".'
        if self.cipher[0] == 'c':
            # Caesar Cipher is a specific shift of 3
            self.key = [3 * self.mode]
        if self.cipher[0] == 'a':
            # Atbash cipher is a specific substitution cipher case
            self.key = list(SYMBOLS)
            self.key.reverse()

    def get_mode(self):
        while True:
            print 'Do you wish to encrypt or decrypt a message?'
            mode = raw_input().lower()
            if mode in ['encrypt', 'e']:
                self.mode = 1
                break
            elif mode in ['decrypt', 'd']:
                self.mode = -1
                break
            else:
                print 'Enter either "(E)ncrypt" or "(D)ecrypt".'

    def get_message(self):
        print 'Enter your message:'
        self.message = raw_input()

    def get_key(self):
        if self.cipher in ['shift', 's']:  # Shift cipher, get numeric key value
            while True:
                print 'Enter the key number (1-{})'.format(MAX_KEY_SIZE)
                key = int(raw_input())
                if key >= 1 and key <= MAX_KEY_SIZE:
                    self.key = [key * self.mode]
                    break
        elif self.cipher in ['substitution', 'u']:
            print 'Enter your seed:'
            seed_init = int(raw_input())
            symbols_list = list(SYMBOLS)
            seed(seed_init)
            shuffle(symbols_list)
            self.key = symbols_list
        elif self.cipher in ['zigzag', 'z']:
            while True:
                print 'Enter number of rails (2-{}):'.format(len(self.message) / 2)
                key = int(raw_input())
                if key > 1 and key <= len(self.message) / 2:
                    self.key = key
                    break
        else:  # Vigenere cipher, get keyword vector
            self.key = []
            print 'Enter your keyword or phrase:'
            keyword = raw_input()
            key = keyword
            while len(key) < len(self.message):  # We will need to repeat the keyword
                key += keyword
            if len(key) > len(self.message):
                key = key[:len(self.message)]
            for symbol in key:
                self.key.append(
                    SYMBOLS.find(symbol) * self.mode
                )

    def do_substitution(self):
        pairing_list = zip(list(SYMBOLS), self.key)
        if self.mode == 1:  # encryption mode
            cipher_dict = {pair[0]: pair[1] for pair in pairing_list}
        else:
            cipher_dict = {pair[1]: pair[0] for pair in pairing_list}
        for symbol in self.message:
            self.translated += cipher_dict[symbol]

    def do_zig_zag(self):
        rails = []
        indices = []
        for i in range(self.key):
            indices.append(i)
        while len(indices) < len(self.message):
            for i in range(self.key - 2, -1, -1):
                indices.append(i)
            for i in range(1, self.key):
                indices.append(i)
        if self.mode == 1:
            for i in range(self.key):
                rails.append([])
            for i in range(len(self.message)):
                rails[indices[i]].append(self.message[i])
            self.translated = ''.join([''.join(rail) for rail in rails])
        else:
            cycle = (self.key * 2) - 2
            full_cycles = len(self.message) / cycle
            leftovers = len(self.message) % cycle
            add_ons = [0 for i in range(self.key)]
            if leftovers > self.key:  # We have more than half an extra cycle
                add_ons = [1 for i in range(self.key)]
                leftovers -= sum(add_ons)
                for i in range(self.key - 2, 0, -1):
                    add_ons[i] += 1
                    leftovers -= 1
                    if leftovers == 0:
                        break
            else:  # Add 1s as needed
                for i in range(self.key):
                    add_ons[i] += 1
                    leftovers -= 1
                    if leftovers == 0:
                        break
            if len(indices) > len(self.message):
                indices = indices[:len(self.message)]
            message = self.message
            for i in range(self.key):
                substring = (2 * full_cycles) + add_ons[i]
                if i == 0:
                    substring = full_cycles + add_ons[i]
                    rails.append(list(message[:substring]))
                elif substring > len(message):
                    rails.append(list(message))
                else:
                    rails.append(list(message[:substring]))
                message = message[substring:]
            for i in indices:
                self.translated += rails[i].pop(0)

    def translate(self):
        if self.cipher in ['substitution', 'u', 'atbash', 'a']:
            self.do_substitution()
        elif self.cipher in ['zigzag', 'z']:
            self.do_zig_zag()
        else:
            self.do_shift()

    def do_shift(self):
        for i in range(len(self.message)):
            symbol_index = SYMBOLS.find(self.message[i])
            translated_symbol_index = symbol_index + self.key[i % len(self.key)]
            if translated_symbol_index >= MAX_KEY_SIZE:
                translated_symbol_index %= MAX_KEY_SIZE
            elif translated_symbol_index <= -MAX_KEY_SIZE:
                translated_symbol_index += MAX_KEY_SIZE
            self.translated += SYMBOLS[translated_symbol_index]

    def run(self):
        self.get_mode()
        self.get_cipher()
        self.get_message()
        if self.cipher[0] not in ['a', 'c']:
            self.get_key()
        self.translate()
        print 'Your translated text is:'
        print self.translated


if __name__ == '__main__':
    CipherMachine().run()
