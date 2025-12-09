num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

if num1 < 0 and num2 < 0:
    print(False)
elif num1 < 0:
    print(num1 + 1000, num2)
elif num2 < 0:
    print(num1, num2 + 1000)
else:
    print(True)