from math import *

aiz26 = { 
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
25:    "Z"
}

a1z26encrypt = {
"A": 1,
"B": 2,
"C": 3,
"D": 4,
"E": 5,
"F": 6,
"G": 7,
"H": 8,
"I": 9,
"J": 10,
"K": 11,
"L": 12,
"M": 13,
"N": 14,
"O": 15,
"P": 16,
"Q": 17,
"R": 18,
"S": 19,
"T": 20,
"U": 21,
"V": 22,
"W": 23,
"X": 24,
"Y": 25,
"Z": 26,
}
def Decrypt(text):
    text =  list(map(int, str(text))) 
    text = list(map(lambda x:x-1, text))
    text = ''.join(list(map(lambda x:aiz26.get(x, "undefined"), text)))
    return text

def Encrypt(text):
    text = list(text.upper())
    text = ''.join(list(map(lambda x:str(a1z26encrypt.get(x, "undefined")), text)))
    return text