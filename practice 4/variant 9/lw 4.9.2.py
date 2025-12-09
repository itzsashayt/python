number = int(input("Введите число: "))

if number > 0:
    if number % 2 == 0:
        print(True, "even")
    else:
        print(True, "odd")
else:
    print(False)