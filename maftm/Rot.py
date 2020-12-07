from  math import *

def Rotate( text, Rotation):
    text = text.lower()
    chars = "abcdefghijklmnopqrstuvwxyz"
    trans = chars[Rotation:]+chars[:Rotation]
    rot_char = lambda c: trans[chars.find(c)] if chars.find(c)>-1 else c
    return ''.join( rot_char(c) for c in text ) 
        