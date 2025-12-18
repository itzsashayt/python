n = int(input("Всего чисел будет: "))

numbers = []

for i in range(n):
    num = int(input())
    numbers.append(num)

result = list(filter(lambda x: x % 3 == 0 and x % 5 == 0, numbers))

print(result)