n = int(input("Введите количество программистов: "))

if n % 10 == 1 and n % 100 != 11:
    ending = ""
elif 2 <= n % 10 <= 4 and not (12 <= n % 100 <= 14):
    ending = "а"
else:
    ending = "ов"

print(f"{n} программист{ending}")