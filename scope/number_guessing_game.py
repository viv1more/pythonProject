# Number Guessing Game Objectives:

# Include an ASCII art logo and random module
import random as rd
from art import guessing_game

# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# setting difficulty for game

def set_difficulty():
    level = input(" Tell Difficulty you want 'hard' or 'easy' ")
    if level == 'hard':
        return HARD_LEVEL_TURNS
    else :
        return EASY_LEVEL_TURNS


# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
def check(guess, mynumber, turns):
    if guess > mynumber:
        print( "Tooo High ")
        return turns - 1
    elif guess < mynumber:
        print( "Too Low ")
        return turns - 1
    else:
        # If they got the answer correct, show the actual answer to the player.
        return f"you got the answer {mynumber}"


def game():
    print(guessing_game)
    print("Welcome to Number Guessing Game ")
    print("I am thinking about number between 1 and 100 !")
    mynumber = rd.randint(1, 100)  # choosing number between 1 to 100


    turns = set_difficulty()
    # Allow the player to submit a guess for a number between 1 and 100.
    guess = 0

    while guess != mynumber:
        print(f"You have {turns} attempts remaining to guess the number.")

        guess = int(input("Guess the Number between 1 and 100 : "))

        turns = check(guess, mynumber, turns)
        # If they run out of turns, provide feedback to the player.
        if turns == 0:
            print("You are run out of guesses ! You Lose" )
            print(f"Sorry the correct answer is {mynumber}")
            return

        elif guess != mynumber:
            print("guess again")

game()
