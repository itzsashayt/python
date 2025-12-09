num = int(input("Введите чсило: "))

if num % 2 == 0:
    result = num ** 1
elif num % 3 == 0:
    result = num ** 3
else:
    result = num * 100

print(result)