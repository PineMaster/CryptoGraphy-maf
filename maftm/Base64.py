from math import *
import textwrap
import binascii

base64table = { 
0:    "A",
1:    "B",
2:    "C",
3:    "D",
4:    "E",
5:    "F",
6:    "G",
7:    "H",
8:    "I",
9:    "J",
10:    "K",
11:    "L",
12:    "M",
13:    "N",
14:    "O",
15:    "P",
16:    "Q",
17:    "R",
18:    "S",
19:    "T",
20:    "U",
21:    "V",
22:    "W",
23:    "X",
24:    "Y",
25:    "Z",
26:    "a",
27:    "b",
28:    "c",
29:    "d",
30:    "e",
31:    "f",
32:    "g",
33:    "h",
34:    "i",
35:    "j",
36:    "k",
37:    "l",
38:    "m",
39:    "n",
40:    "o",
41:    "p",
42:    "q",
43:    "r",
44:    "s",
45:    "t",
46:    "u",
47:    "v",
48:    "w",
49:    "x",
50:    "y",
51:    "z",
52:    "0",
53:    "1",
54:    "2",
55:    "3",
56:    "4",
57:    "5",
58:    "6",
59:    "7",
60:    "8",
61:    "9",
62:    "+",
63:    "/"
}

def Encrypt(text):
    characters = list(text)
    characters = map(lambda  x: format(ord(x), '08b'), characters)
    #Convert to binary--------
                                                                        #for character in text:
                                                                        #    characters += [str(format(ord(character),'08b'))]


    #block into blocks of 6, padding etc-------------------
    characters = ''.join(characters)
    characters = textwrap.wrap(characters, 6)
    paddings = 0
    tmp_characters = []
    for character in characters:
        if paddings == 4:
            paddings = 0

        if not len(character) == 6:
            addzero = 6 - len(character)
            character = character + (str(0) * addzero)
        tmp_characters += [character]
        paddings += 1

    characters = tmp_characters
    #convert to int and ascii table----------------
    dummy = 0
    for character in characters:
        characters[dummy] = base64table[int(characters[dummy], 2)]
        dummy += 1
    if not paddings == 4:
        paddings = 4-paddings
        characters += [paddings*"="] 

    # apply padding
    characters = ''.join(characters)
    #return
    return characters


def Decrypt(ciphertext):
    ciphertext = str(ciphertext).strip("=")
    characters = []
    key_list = list(base64table.keys()) 
    val_list = list(base64table.values())
    for character in ciphertext:
        tmp = bin(int(key_list[val_list.index(character)]))[2:]
        if len(tmp) != 6:
            tmp = (6 - len(tmp)) * "0" + tmp  
        characters += [tmp]

    padding = 0
    for word in characters:
        for alphabets in word:
            padding += 1
            if padding == 8:
                padding = 0
    if padding != 0:
        characters[-1] = characters[-1][:-padding]
    characters = ''.join(characters)
    characters = textwrap.wrap(characters, 8)

    tmp_characters = []
    for character in characters:
        character = int(character, 2)
        character = character.to_bytes((character.bit_length() + 7) // 8, 'big').decode()
        tmp_characters += [character]
    characters = tmp_characters
    characters = ''.join(characters)
    return characters