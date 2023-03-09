#!/usr/bin/python3
consonants = "qwrtpsdfghjklzxcvbnm" # This is fine don't need a list of a string.
summer_word = "icecream"

new_word = ""

for character in summer_word: # loop through each character in summer_word
    if character in consonants: # check whether the character is in the consonants list
        new_word += character
    else:
        continue # Not really necessary by adds structure. Just says do nothing if it isn't a consonant.

ANSWER = new_word
print("{:s}".format(ANSWER))
