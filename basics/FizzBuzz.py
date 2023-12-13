# FizzBuzz

# print the numbers from 1 to 100 and check for fizzbuzz

# if number is divisible by 3 its Fizz
# if number is divisible by 5 its Buzz
# and if number divisible both by 3 & 5 then its FizzBuzz

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
