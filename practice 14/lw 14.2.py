any_list = [4, 3.2, 16, 9, 13.5, 67]

print("Выходные данные: ")

for index, value in enumerate(any_list):
    try:
        result = value / index
        print(f"{value} / {index} = {result}")
    except ZeroDivisionError:
        print(f"Деление на 0! Элемент: {value}")