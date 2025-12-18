__numbers = lambda n, step=1: [[[n + (i*2 + j)*step] for j in range(2)] for i in range(2)]

def print_field(n, step=1):
    field = __numbers(n, step)
    for row in field:
        print(" ".join(f"[{elem[0]}]" for elem in row))

print("Пример 1:")
print_field(1)

print("\nПример 2:")
print_field(1, 3)