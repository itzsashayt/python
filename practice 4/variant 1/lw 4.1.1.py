num = int(input("Введите целое число: "))


if num < 0:

    result = abs(num)
    print(f"Преобразованное число: {result}")
elif num == 0:
   
    result = 1
    print(f"Преобразованное число: {result}")
else:
 
    print(f"Число: {num}")