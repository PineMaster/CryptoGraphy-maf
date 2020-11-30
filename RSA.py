import tqdm
import sys
from math import *
 

def SieveOfEratosthenes(n, isPrime) :
 
    isPrime[0], isPrime[1] = False, False
 
    for i in range(2, n + 1) :
        isPrime[i] = True
 
    for p in range(2, int(sqrt(n)) + 1) :
 
        if isPrime[p] == True :
 
            for i in range(p * 2, n + 1, p) :
                isPrime[i] = False

def findPrimePair(n) :
 
    flag = 0
     
    isPrime = [False] * (n + 1)
    SieveOfEratosthenes(n, isPrime)
 
    for i in range(2, n) :
        x = int(n / i)
 
        if (isPrime[i] & isPrime[x] and
             x != i and x * i == n) :
            flag = 1
            return i, x
 
    if not flag :
        print("No such pair found")

def CoPrimes(n,phi):
    for number in range(2, phi):
        if(gcd(number,int(n)) == 1 and gcd(number,int(phi)) == 1):
            return number 

def Decrypt(d,n, inpu):
    output = ""
    for character in inpu:
        output += str((int(character) ** d) % n)
    return output


    
encryptionkey = input("Give modulis variable <n>, this will try to calculate e and d: ").split()

for key in encryptionkey:
    if(not key.isdigit()):
        print("Invalid key, exiting...")
        sys.exit()
if(not len(encryptionkey) == 1):
    if(not key.isdigit()):
        print("Invalid key, exiting...")
        sys.exit()

n = int(encryptionkey[0])
#n = int(encryptionkey[1])

p, q = findPrimePair(n)

phi = (q-1)*(p-1)
e = CoPrimes(n, phi)
print(phi)
print(e)
dum=0
while True:
    dum = dum +1
    d = (dum * e) % phi
    if(d == 1):
        d = dum
        break


print("Found decryption key:", d)

ciphertext = input("Gimme ciphertext: ")
characterset = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

ciphertext_num = ""
for character in ciphertext:
    ciphertext_num += str(characterset.find(character.upper())+1)

text_num = Decrypt(d, n, ciphertext_num)
text=""

for character in text_num:
    text += characterset[int(character)-1]

print(text)