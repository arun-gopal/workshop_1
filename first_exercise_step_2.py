def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def mod(x, y):
    return x % y

def calculate(operation, first_operand, second_operand):
    if operation == '+':
        result = add(first_operand, second_operand)
        print(f"{first_operand} {operation} {second_operand} = {result}")
        return result

    elif operation == '-':
        result = subtract(first_operand, second_operand)
        print(f"{first_operand} {operation} {second_operand} = {result}")
        return result

    elif operation == '*' or operation == 'x':
        result = multiply(first_operand, second_operand)
        print(f"{first_operand} {operation} {second_operand} = {result}")
        return result

    elif operation == '/':
        result = divide(first_operand, second_operand)
        print(f"{first_operand} {operation} {second_operand} = {result}")
        return result
    
    elif operation == '%':
        result = mod(first_operand, second_operand)
        print(f"{first_operand} {operation} {second_operand} = {result}")
        return result

    else:
        print('You have not provided a valid operator, please run the program again.')
        return 0

with open("step_2.txt", 'r') as f:
    result = 0
    for line in f:
        line = line.strip().strip('calc ')
        commands = line.split()
        result = result + calculate(commands[0], int(commands[1]), int(commands[2]))
    print(result)

