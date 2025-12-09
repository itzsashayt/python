length1 = float(input("Введите длину первого отрезка: "))
length2 = float(input("Введите длину второго отрезка: "))

if length1 > length2:
    print(f"Первый отрезок длинее на {length1 - length2}")
elif length2 > length1:
    print(f"Второй отрезок длинее на {length2 - length1}")
else:
    print("Отрезки равны")