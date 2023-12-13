import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
           'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
           '_', '+', '-', '=', '{', '}', '[', ']', '|', '\\',
           ';', ':', '\'', '"', '<', '>', ',', '.', '/', '?']

print("__ Welcome to My Random Password Generator __")

no_letters = int(input("How Many Letters you want in your password ? "))

no_numbers = int(input("How Many numbers you want in your password ? "))

no_symbols = int(input("How symbols Letters you want in your password ? "))

password = ""

# Easy Level
'''for char in range ( 1, no_letters+1):
    password+=random.choice(letters)

for char in range (1, no_numbers+1 ):
    password+=random.choice(numbers)

for char in range(1, no_symbols + 1):
        password += random.choice(symbols)
print(password)'''

# hard level

password_list = []
for char in range(1, no_letters + 1):
    password_list += random.choice(letters)

for char in range(1, no_numbers + 1):
    password_list += random.choice(numbers)

for char in range(1, no_symbols + 1):
    password_list += random.choice(symbols)
# print(password_list)

random.shuffle(password_list)

# print(password_list)


for char in password_list:
    password += char
print(f"Your randomly generated password is {password}")
