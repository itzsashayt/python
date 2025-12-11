A = [
    [-446, 281, -80],
    [465, 432, -122],
    [13, "error", 8]
]

print("Исходная матрица:")
for row in A:
    print(row)

for i, row in enumerate(A):
    for j, element in enumerate(row):
        if isinstance(element, str):
            A[i][j] = len(element)

print("\nМатрица после замены слова на количество символов:")
for row in A:
    print(row)

total_sum = 0
for row in A:
    for element in row:
        total_sum += element

print(f"\nСумма всех элементов матрицы: {total_sum}")