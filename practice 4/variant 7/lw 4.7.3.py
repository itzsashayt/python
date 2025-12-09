num = int(input("Введите число: "))
last_digit = abs(num % 10)

if last_digit == 0:
    result = num ** 10
elif last_digit == 1:
    result = num % 3
elif last_digit == 2:
    result = num // 2
else:
    result = num ** 2
    
print(result)