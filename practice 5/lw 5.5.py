negative_numbers = []
positive_numbers = []
zeros = []

n = int(input("Введите количество чисел: "))

for i in range(n):
    num = int(input("Введите число: "))

    if num < 0:
        negative_numbers.append(num)
    elif num > 0:
        positive_numbers.append(num)
    else:
        zeros.append(num)

        print("\nРаспределение по спискам:")
        print("Отрицательные числа:", negative_numbers)
        print("Положительные числа:", positive_numbers)
        print("Нули", zeros)


        sum_negative = sum(negative_numbers)
        print(f"\nСумма отрицательных чисел {sum_negative}")

        if len(positive_numbers) > 0:
            average_positive = sum(positive_numbers) / len(positive_numbers)
            print(f"Среднее арифетическое положительных чисел: {average_positive:.1f}")
        else:
            print("Положительных чисел нет")

            if len(zeros) > 0:
                stars_list = ['*' for _ in zeros]

                print(f"Количество звёзд: {len(stars_list)} {stars_list}")
            else:
                print("Нулей нет")