number1 = 0
number2 = 0
result = 0
operation = ''

while True:

    number1 = int(input('Digite o numéro: '))
    operation = input('Digite a operação (+, -, /, *): ')
    number2 = int(input('Digite o número: '))

    if operation == '+':
        result = number1 + number2
    elif operation == '-':
        result = number1 - number2
    elif operation == '/':
        result = number1 / number2
    elif operation == '*':
        result = number1 * number2
    else:
        result = 'Operação inválida'

    print(str(number1) + ' ' + str(operation) + ' ' + str(number2) + ' = ' + str(result))




  

