print("--------------------------------------------------")
print("------------ ---|| Treasure Hunt ||--- -----------")
print("--------------------------------------------------")
print ('''


                    ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
             \_________        \####/      _________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\\u//.-'    __/ \__ |
              |==== .'.'^'.'.====|
              |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`
''')
print("You are in a mansion on the search for treasure. Where would you like to search?  ")
choice1 = input("Type left or right and hit 'Enter'".lower())

if choice1 == "left":
  print("Swim or wait?")
  choice2 = input("Type swim or wait and hit 'Enter'.)".lower())
  if (choice2 == "wait"):
    print("Which door?")
    choice3 = input("Type red, blue, or yellow and hit 'Enter'".lower())
    if (choice3 == "yellow"):
      print("Congratulations ! You win!👌👌👌👌👌")
    else:
      print("Game over!")
  else:
    print("Attacked by trout. Game over.")
else:
  print("You fell into a hole. Game Over.")
