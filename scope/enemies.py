enemies = 1  # global Scope
friends = 5


# namespaces are valid in certain scope
def increase_enemies():
    enemies = 5  # local Scope
    friends = 6
    print(f" Enemies inside functions are {enemies}")
    print(f" We have {friends} Friends inside  ")  # global variable used

    def war_inside():
        if enemies > friends:
            return "we Lose"
        elif friends > enemies:
            return 'We win'
        else:
            return "draw"
    print(f" {war_inside()} inside battle ")

print(f" Enemies outside room are {enemies}")
print(f" We have {friends} Friends outside")

def war_outside():
    if enemies > friends:
        return "we Lose"
    elif friends > enemies:
        return 'We win'
    else:
        return "draw"
increase_enemies()
print(f" {war_outside()} outside battle ")
