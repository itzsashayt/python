try:
    total_minutes = int(input())
except ValueError:
    print("Ошибка: Введите целое число минут.")
    exit()

hours = total_minutes // 60

minutes = total_minutes % 60

print(hours)
print(minutes)

