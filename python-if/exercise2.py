# La fonction type() affiche le type de donnees
# d'une valeur (chaine, entier, booleen...)

print(type('Hello World'))
print(type(7))

print(type(True))
print(type(False))

print(type('True'))
print(type('False'))

# La fonction bool() convertit differentes valeurs de chaine
# en valeurs booleennes.
# Si la fonction est fournie avec une chaine vide elle retourne False,
# pour toute autre valeur elle retournera True.

print(bool('True'))
print(bool('False'))
print(bool(''))
print(bool(' '))
print(bool('Hello World!'))

# La fonction bool() convertit differentes valeurs de nombres entiers
# en valeurs booleennes.
# Si la fonction est fournie avec un 0 elle retourne False,
# pour toute autre valeur elle retournera True.

print(bool(7))
print(bool(1))
print(bool(0))
print(bool(-1))

# Ce code evalue le resultat d'une expression booleenne

print(1 + 1 == 3)
print(1 + 1 == 2)

print(3 == 4)
print(3 != 4)

print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)


first_number = 5
second_number = 0
true_value = True
false_value = False

if first_number > 1 and first_number < 10:
    print('The value is between 1 and 10.')

if first_number > 1 or second_number > 1:
    print('At least one value is greater than 1')

print(not true_value)
print(not false_value)

if not first_number > 1 and second_number < 10:
    print('Both values pass the test')
else:
    print('Both values do NOT pass the test')
