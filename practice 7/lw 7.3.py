bin_sy = ['11011111', '11011101', '11000111', '11011100', '11011110']

decimal_numbers = []

print("Двоичные числа и их десятичные эквиваленты:")


for binary in bin_sy:

    decimal = int(binary, 2)
    decimal_numbers.append(decimal)
    
    print(f"{binary} = {decimal}")

max_num = max(decimal_numbers)
min_num = min(decimal_numbers)

print(f"\nМаксимальное число: {max_num}")
print(f"Минимальное число: {min_num}")