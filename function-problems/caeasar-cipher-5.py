alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ''
    if cipher_direction == 'decode':
        shift_amount *= -1  # shift_amount= shift_amount * -1

    for char in start_text:
        if char in alphabet:
            pos = alphabet.index(char)

            new_pos = pos + shift_amount
            end_text = end_text + alphabet[new_pos]

        else:
            end_text += char

    print(f"The {cipher_direction}ed text is {end_text}")


# TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
should_continue = True
while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    result = input("Do You want to Continue ? yes or no ... .\n")

    if result == 'no':
        should_continue = False

        print("Good Bye !!!")
