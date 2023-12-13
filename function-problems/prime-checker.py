# Program to check the number is prime or not

num = int(input("Enter the Number you want "))


def prime_checker(number):

    is_prime =True   #boolean variable for checking

    for i in range (2 , number):   #looping through 2 to given number
        if number % i == 0:
             is_prime = False      #wont execute this part if false

    if is_prime:                   #if is_prime == True then checks the condition

        print(f"{number} is Prime Number ")

    else:

        print(f"{number} is not Prime Number ")

prime_checker(number = num )
