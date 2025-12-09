num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

if num1 > num2:
    result = num1 ** num2
elif num2 > num1:
    result = num2 ** num1
else:
    result = num1 + num2

print(result)