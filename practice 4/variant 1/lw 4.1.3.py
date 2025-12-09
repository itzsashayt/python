num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

divisible1 = num1 % 3 == 0
divisible2 = num2 % 3 == 0

if divisible1 and divisible2:
    print(True)
elif divisible1 or divisible2:
    print("Одно число делится на 3")
else:
    print(False)