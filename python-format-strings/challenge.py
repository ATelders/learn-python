first_value = '  FIRST challenge         '
second_value = '-  second challenge  -'
third_value = 'tH IR D-C HALLE NGE'

fourth_value = 'fourth'
fifth_value = 'fifth'
sixth_value = 'sixth'

# First challenge
first_value = '       ' + (first_value.strip()).title()

# Second challenge
second_value = ((second_value.replace('-', ' ')).strip()).capitalize()

# Third challenge
third_value =  '\t       ' + ((third_value.replace(' ', '')).replace('-', ' ')).capitalize()

print(first_value)
print(second_value)
print(third_value)

# Fourth challenge - use only the print() function (no f-strings)
print(fourth_value, fifth_value, sixth_value, sep='#', end='!')

# Fifth challenge - use only a single print() function.  Create tabs and new lines using f-strings.

print(f'\n\t{fourth_value}\n\t{fifth_value}\n\t{sixth_value}\n')