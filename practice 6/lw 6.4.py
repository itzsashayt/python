random_elements = [
    ['toy', 'bee', 'cheese', 'car'],
    [False, 'word', '0110110', 10],
    ['happiness', '(1 *P*)', 'luck', None],
    ['car', '<- code ->', 4.7, True]
]

for row_index, row in enumerate(random_elements):
    for col_index, element in enumerate(row):
        if col_index % 2 == 1: 
            print(f"Строка {row_index}, столбец {col_index}: {element}")