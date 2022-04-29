# Author: mMamoun Janfor


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

#- make sure the user enter encode or decode
dir = True
while dir:
    if direction == "encode" or direction == "decode":
       dir = False
    else:
       direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n") 

text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#-1: Create a function called 'encrypt_decrypt' that takes the 'text' and 'shift' as inputs.
def encrypt_decrypt(direction1, text1, shift1,):
    cipher = ''
    if direction1 == "encode":
        for l in text1:
            i = alphabet.index(l)
            b = i + shift1
            if b <= 25:
                cipher  += alphabet[b]
            elif b > 25:
                c = 26 - i
                e = shift1 - c
                cipher += alphabet[e]
            
        print(f"the encrypted word is: {cipher}")

    elif direction1 == "decode":   
        for l in text1:
            i = alphabet.index(l)
            b = i - shift1
            
            cipher  += alphabet[b]
            
        print(f"the decrypted word is: {cipher}")
    else:
        print("you must enter encrypt or decrypt")

#- calling the fucntion
encrypt_decrypt(direction, text, shift)

    