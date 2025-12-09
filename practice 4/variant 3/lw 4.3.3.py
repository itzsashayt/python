a = float(input("Введите первую сторону: "))
b = float(input("Введите вторую сторону: "))
c = float(input("Введите третью сторону: "))

if a <= 0 or b <= 0 or c <= 0:
    print("Стороны должны быть положительными!")
elif a + b <= c or a + c <= b or b + c <= a:
    print("Такого треугольника не существует!")
else:
    if a == b == c:
        print("Равносторонний")
    elif a == b or b == c or a == c:
        print("Равнобедренный")
    else:
        print("Разносторонний")