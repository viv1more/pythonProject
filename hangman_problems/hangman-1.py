# Step 1
import random

word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

chosen_word = random.choice(word_list)  # Choose random word from list

print(chosen_word)

guess = input("Enter the letter want to check: ").lower()

for char in chosen_word:  # check for every character in chosen_word
    if char == guess:  # check if char matches guess of user
        print(f"{char} = Right..")
    else:
        print(f"{char} = Wrong..")
