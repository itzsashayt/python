fruits = [['Banana', 'apple'], ['apricot', 'Avocado'], ['lime', 'lemon'], ['Mango', 'grapes']]

for row in fruits:
    for fruit in row:
        if fruit[0].isupper():
            print(fruit)