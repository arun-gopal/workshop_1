def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

operation = input('What operation do you want to perform? ')
first_operand = int(input('What is the first operand? '))
second_operand = int(input('What is the second operand? '))

if operation == '+':
    print(add(first_operand, second_operand))

elif operation == '-':
    print(subtract(first_operand, second_operand))

elif operation == '*':
    print(multiply(first_operand, second_operand))

elif operation == '/':
    print(divide(first_operand, second_operand))

else:
    print('You have not provided a valid operator, please run the program again.')

