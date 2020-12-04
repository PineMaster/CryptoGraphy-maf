from maftm import A1Z26, Base64, RSA
cipherType = input("What cipher would you like to do? Type 1 for RSA, 2 for AZ126, and 3 for BASE64. ")
if cipherType == "1":
    n = int(input("Gimme dat modulus variable: "))
    d, e = RSA.GetKeys(n)
    ciphertext = input("Gimme Ciphertext: ")
    Decrypted_text = RSA.Decrypt(d, n, ciphertext)
    print(Decrypted_text)
    

elif cipherType == "2":
    cipher = input("Gimme cipher: ")
    decrypted  = A1Z26.Decrypt(cipher)
    print(decrypted)
elif cipherType == "3":
    cipher = input("Gimme cipher: ")
    decrypted  = Base64.Decrypt(cipher)
    print(decrypted)
