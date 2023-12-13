import random

print("Lets See Who is going to pay today's bill ...... ")
name_input = input("Enter Everyone's Name Separated by comma : ")

name = name_input.split(", ")  # used to split the string into list

print(name)

# print(len(name))

random_choice = random.randint(0, len(name) - 1)  # -1 is used because it will check the index

# print(random_choice)

print(f"{name[random_choice].upper()} is our brother who is going to pay our today's bill 😁😁😁😁😁😁😘😘😘😘 ")
