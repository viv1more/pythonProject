"""list2 = ["Red", "Green", "Blue", "Yellow", "Pink"]

for color in list2:
    print(color, end=' ')
    print("Color")

"""

total = 0
a = int(input("Enter the Starting range number: "))
b = int(input("Enter the Ending range number: "))

print(f"Sum of numbers from {a} to {b}:")

for number in range(a, b + 1):
    total = total + number
    if number < b:
        print(f"{number} + ", end='')
    else:
        print(f"{number} ", end='')

print(" = ", total)
