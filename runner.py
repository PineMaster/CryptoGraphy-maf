from maftm import A1Z26, Base64, RSA
cipherType = input("What cipher would you like to do? Type 1 for RSA, 2 for AZ126, and 3 for BASE64. ")
if cipherType == "1":
    n = int(input("Gimme dat modulus variable: "))
    int(n)
    d, e = RSA.GetKeys(n)
    ciphertext = input("Gimme Ciphertext: ")
    Decrypted_text = RSA.Decrypt(d, n, ciphertext)
    print(Decrypted_text)
    


