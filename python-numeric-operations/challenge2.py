print('Simple calculator!')
number1 = input('First number?  ')
operation = input('Operation?  ')
number2 = input('Second number?  ')

if number1.isnumeric == False or number2.isnumeric == False :
    print('Please input a number')
    exit()

number1 = float(number1)
number2 = float(number2)

if operation == '+' :
    print(f'Sum of {number1} and {number2} is {number1 + number2}')
elif operation == '-' :
    print(f'Difference of {number1} and {number2} is {number1 - number2}')
elif operation == '*' :
    print(f'Product of {number1} and {number2} is {number1 * number2}')
elif operation == '/' :
    print(f'Quotient of {number1} and {number2} is {number1 / number2}')
elif operation == '**' :
    print(f'Exponent of {number1} and {number2} is {number1 ** number2}')
elif operation == '%' :
    print(f'Modulus of {number1} and {number2} is {number1 % number2}')
else :
    print('Operation not recognized')
    exit()
