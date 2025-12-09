num = int(input("Введите число: "))

if num < 0:
    pass
elif num > 100:
    print("*")
else:
    print("*" * num)