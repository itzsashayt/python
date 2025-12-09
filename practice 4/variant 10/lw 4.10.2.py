number = int(input("Введите целое число: "))

if number < 0:
    number = 1_000_000
    print(number)
elif number == 0:
    number = 2
    result = number ** 2
    print(result)
else:
    result = number ** 3
    print(result)