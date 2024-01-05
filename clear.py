from os import system, name


# define our clear function
def clear():

    if name == 'nt':
        _ = system('cls')

    # and for mac and linux, the os.name is 'posix'
    else:
        _ = system('clear')

# Then, whenever you want to clear the screen, just use this clear function as:
clear()