alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(txt=text, shft=shift):
    cipher_txt = ''  # to  store cipher text

    for letter in txt:  # checks every letter in string
        pos = alphabet.index(letter)  # position is index of letter in alphabet list
        new_pos = pos + shft  # adding places we shifted
        new_letter = alphabet[new_pos]  # creates new letter by selecting updated position
        cipher_txt += new_letter  # inserts cipher text to new letter
    print(f"The Encrypted word is : {cipher_txt}")


#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

def decrypt (txt=text, shft=shift):

    decrypted_txt = " "

    for letter in txt:
        pos =alphabet.index(letter)
        # TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards*
        # in the alphabet by the shift amount and print the decrypted text.
        new_pos = pos - shift
        new_letter = alphabet[new_pos]
        decrypted_txt+=new_letter
    print(f"The Decrypted word is {decrypted_txt}")


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.

if direction == 'encode':
    encrypt(text,shift)
elif direction == 'decode':
    decrypt(text,shift)