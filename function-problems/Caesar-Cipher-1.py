alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

'''TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.'''


def encrypt(txt = text, shft = shift):
    """ TO DO - 2: Inside the \'encrypt\' function, shift each letter of the \'text\' forwards \n'
    in the alphabet by the shift amount and print the encrypted text.  ')"""
    # e.g.
    # plain_text = "hello"
    # shift = 5
    # cipher_text = "mjqqt"
    # print output: "The encoded text is mjqqt"

    cipher_txt = ''  # to  store cipher text


    for letter in txt:  #checks every letter in string
        pos = alphabet.index(letter) #position is index of letter in alphabet list
        new_pos = pos + shft   # adding places we shifted
        new_letter = alphabet[new_pos]   # creates new letter by selecting updated position
        cipher_txt+= new_letter     #inserts cipher text to new letter
    print(f"The Encrypted word is : {cipher_txt}")


##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

'''TODO-3: Call the encrypt function and pass in the user inputs. 
You should be able to test the code and encrypt a message.'''

encrypt(text, shift)