from art import calclogo


def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mult(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


operations = {

    "+": add,
    "-": sub,
    "*": mult,
    "/": div
}


def calculator():
    print(calclogo)
    num1 = float(input("Enter the First Number: "))

    for _ in operations:

        should_continue = True

    while should_continue:
        operation_symbol = input('Choose the operation from the above ')
        num2 = float(input("Enter Second Number: "))

        calculation_function = operations[operation_symbol]

        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"type 'y' to calculate with {answer}, or 'n' to start new calculation ") == 'y':

            num1 = answer
        else:

            should_continue = False
            calculator()  # recursion


calculator()
