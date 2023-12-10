# program to print sum of even numbers
total = 0
for even in range(1, 101):

    if even % 2 == 0:
        total = total + even
        if even < 100:
            print(f"{even}+", end='')
        else:
            print(f"{even} ", end='')

print(f"= {total}")
