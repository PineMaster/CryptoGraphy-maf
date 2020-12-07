import sys
from math import *
 
def encrypt(text, key):
    if(not len(str(key)) == 8):
        raise Exception("invalid key")
    for character in str(key):
        if(not character in "10"):
            raise Exception("invalid key")

    text, key = list(str(text)),list(str(key))
    key = list(map(int, key))
    text = list(map(lambda  x: format(ord(x), '08b'), text))
    
    ciphertext = []
    ciphertext2 = []
    for characters in text:
        characters = list(characters)
        i = 0
        new_characters = ""
        for character in characters:
            if int(character) == key[i]:
                new_characters += "0"
            else:
                new_characters += "1"
            i += 1
        ciphertext2 += [new_characters]
        new_characters = chr(int(new_characters.lstrip("0"), 2))
        ciphertext += [new_characters]


    return ''.join(ciphertext), '-'.join(ciphertext2)


def decrypt(ciphertext, key):
    ciphertext = str(ciphertext).split("-")
    key = str(key)
    text = []
    text2 = []
    for word in ciphertext:
        i = 0
        new_word = ""
        for character in word:
            if str(character) == str(key[i]):
                new_word += "0"
            else:
                new_word += "1"
            i += 1
        text += [new_word]
        text2 += [chr(int(new_word.lstrip("0"), 2))]
    return ''.join(text2), '-'.join(text)

    