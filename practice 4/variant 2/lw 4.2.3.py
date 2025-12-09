r = int(input("Введите значение R (0-255): "))
g = int(input("Введите значение G (0-255): "))
b = int(input("Введите значение B (0-255): "))

if r == 0 and g == 0 and b == 0:
    print("Чёрный цвет")
elif r == 255 and g == 255 and b == 255:
    print("Белый цвет")
elif r == 255 and g == 0 and b == 0:
    print("Красный цвет")
elif r == 0 and g == 255 and b == 0:
    print("Зелёный цвет")
elif r == 0 and g == 0 and b == 255:
    print("Синий цвет")
else:
    print("Нет цвета")