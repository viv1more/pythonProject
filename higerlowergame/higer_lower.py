import random as rd
from art import higher_lower_logo, vs
from gamedata import data


# Generate a random account from the game data.

def rand_acc():
    random_account = rd.choice(data)
    return random_account


rand_acc()


# Format account data into printable format.
def data_format(account):
    name = account["name"]
    country = account["country"]
    description = account['description']

    return f"{name}  {description} from {country}"


def check_answer(guess, a_followers, b_followers):
    """Checks followers against user's guess
  and returns True if they got it right.
  Or False if they got it wrong."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


def game():
    print(higher_lower_logo)  # Add art.
    score = 0
    game_should_continue = True
    account_a = rand_acc()
    account_b = rand_acc()

    # Make game repeatable.
    while game_should_continue:

        account_a = account_b
        account_b = rand_acc()

        while account_a == account_b:
            account_b = rand_acc()  # Make B become the next A.

            print(f"Compare {data_format(account_a)}{vs}{data_format(account_b)}")
            # Ask user for a guess.
            guess = input("Who has More Followers ? Type 'A' or 'B'").lower()
            ## Get follower count.
            a_follower_count = account_a["follower_count"]
            b_follower_count = account_b["follower_count"]

            is_correct = check_answer(guess, a_follower_count, b_follower_count)

            print(higher_lower_logo)

            # Score Keeping.
            if is_correct:
                score += 1
                # Check if user is correct.

                print(f"You are right ! Your Current Score is {score}.")

            else:
                game_should_continue = False

                print(f"Sorry ! Thats Wrong , Your Final Score is {score}")  # Feedback.


game()
