matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Матрица 3х3:")
for row in matrix:
    print(row)

diagonal_sum = 0
for i in range(len(matrix)):
    diagonal_sum += matrix[i][i]
print(f"\nСумма элементов по главной диагонали: {diagonal_sum}")