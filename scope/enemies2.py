enemies = 1
MYNAME = "Vivek Ashok More"


def increase_enemies():
    #
    # global enemies  #golabllizing local namespace
    # enemies+= 4
    print(f"Enemies of {MYNAME} inside function : {enemies}")
    return enemies + 4



enemies = increase_enemies()
print(f" Now total enemies are,{enemies}")

