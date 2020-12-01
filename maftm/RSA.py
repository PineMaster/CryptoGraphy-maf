import sys
from math import *
 







def GetKeys(n):

    flag = 0

    # sieve of erathonesis to check primes----------
    isPrime = [False] * (n + 1)
    isPrime[0], isPrime[1] = False, False
 
    for i in range(2, n + 1) :
        isPrime[i] = True
 
    for p in range(2, int(sqrt(n)) + 1) :
 
        if isPrime[p] == True :
 
            for i in range(p * 2, n + 1, p) :
                isPrime[i] = False


    # checking for q and q ---------------------------
    for i in range(2, n) :
        x = int(n / i)
 
        if (isPrime[i] & isPrime[x] and x != i and x * i == n) :
            flag = 1

            p = i  #i dunno man couldnt do maf so i copy pasted stuff
            q = x

    if not flag :
        raise Exception("couldnt find p and q")


    # finding e-------------------------------------
    phi = (q-1)*(p-1)
    for number in range(2, phi):
        if(gcd(number,int(n)) == 1 and gcd(number,int(phi)) == 1):
            e = number 

    print("starting to calculate d, this may take a while with larger numbers...")
    d=0
    while True:
        d = d +1
        result = (d * e) % phi
        if(result == 1):
            break
    return d, e 

def Decrypt(d, n, ciphertext):
    characterset = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    ciphertext_num = ""
    for character in ciphertext:
        ciphertext_num += str(characterset.find(character.upper())+1)

    text_num = ""
    for character in ciphertext_num:
        text_num += str((int(character) ** d) % n)
    text=""

    for character in text_num:
        text += characterset[int(character)-1]

    return text

def Encrypt(e, n, text):
    characterset = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    text_num = ""
    for character in text:
        text_num += str(characterset.find(character.upper())+1)

    ciphertext_num = ""
    for character in text_num:
        ciphertext_num += str((int(character) ** e) % n)
    ciphertext=""

    for character in ciphertext_num:
        ciphertext += characterset[int(character)-1]

    return ciphertext