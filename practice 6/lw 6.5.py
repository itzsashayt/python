rows = int(input("Введите количество строк: "))

cols = int(input("Введите количество столбцов: "))

matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        value = int(input(f"Введите значение элемента [{i}][{j}]: "))

        row.append(value)

        matrix.append(row)

        print("\nВаш двумерный массив:")
    for row in matrix:
        print(row)