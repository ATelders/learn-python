fahrenheit = input('What is the temperature in fahrenheit?  ')
if fahrenheit.isnumeric() == False :
    print('Input is not a number')
    exit()

fahrenheit = int(fahrenheit)

celsius = (fahrenheit - 32) * 5/9

celsius = round(celsius)

print(f'Temperature in Celsius is {celsius}')
