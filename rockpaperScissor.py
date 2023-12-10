import random

choice = int(input("Enter your choice 0 for Rock, 1 for Paper and 2 for Scissors: "))
Rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

Paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

Scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

if choice == 0:
    print(f"You Choose Rock {Rock}")
elif choice == 1:
    print(f"You Choose Paper{Paper}")
elif choice == 2:
    print(f"You Choose Scissors{Scissors}")
else:
    print("Naughty ho rha hai kya bkl 😠😠😠😠😠.. ")

# Now Computer's Turn

computerchoice = [Rock, Paper, Scissors]

listlength = len(computerchoice)

randomchoicePC = random.randint(0, listlength - 1)
if choice <= 2:  # Because user can give value more than 2 still computer choose
    if randomchoicePC == 0:
        print(f"Computer Choose Rock {Rock}")
    elif randomchoicePC == 1:
        print(f"Computer Choose Paper{Paper}")
    elif randomchoicePC == 2:
        print(f"Computer Choose Scissors{Scissors}")

# Checking if there is possibility of Draw

if choice == randomchoicePC:
    print(" ---------------------------------")
    print("| There is a Draw........🤏🤏🤏   |")
    print(" ---------------------------------")
# Now the real game starts

if (choice == 0 and randomchoicePC == 1) or (choice == 1 and randomchoicePC == 2) or (
        choice == 2 and randomchoicePC == 0):
    print(" _________________________________")
    print("| Ohh No 😒😒😒!!! Computer Wins |")
    print(" ---------------------------------")

if (choice == 0 and randomchoicePC == 2) or (choice == 1 and randomchoicePC == 0) or (
        choice == 2 and randomchoicePC == 1):
    print(" ________________________________________")
    print("| Congratulations👌👌🍾🍾🎉 !!! You Win |")
    print(" ----------------------------------------")

# made by itsvivekmore
