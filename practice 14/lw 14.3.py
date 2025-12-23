numbers_list = []

numbers_added_count = 0

print("Введите числа (всего 5 чисел будет добавлено в список):")

while numbers_added_count < 5:
    user_input = input (">>>")

    try:
        number = int(user_input)
        numbers_list.append(number)
        numbers_added_count += 1
    except ValueError:
        print("Это не число. Пожалуйста, введите число.")

print("\nПример выходных данных:")
print(f">>> Числа в списке: {numbers_list}")