number1 = int(input('enter first number: '))
number2 = int(input('enter second number: '))
number3 = int(input('enter third number: '))
number4 = int(input('enter fourth number: '))
operation = input('please select the operation +,-,*,/: ')
if operation == '+':
    result = number1 + number2 + number3 + number4
    print(number1, '+', number2, '+', number3, '+', number4, '=', result)
elif operation == '-':
    result_2 = number1 - number2 - number3 - number4
    print(number1, '-', number2, '-', number3, '-', number4, '=', result_2)
elif operation == '*':
    result_3 = number1 * number2 * number3 * number4
    print(number1, '*', number2, '*', number3, '*', number4, '=', result_3)
elif operation == '/':
    result_4 = number1 / number2 / number3 / number4
    print(number1, '/', number2, '/', number3, '/', number4, '=', result_4)
else:
    print('wrong condition ')

