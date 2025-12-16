s1 = {'</>': 13, 'script': 1, '__init__': 10, 'self': 5, 'number_9': 6, '#comment': 100}
print("Исходный словарь:")
print(s1)

key = input("key: ")
value = input("value: ")
s1[key] = int(value) if value.isdigit() else value

print("Обновлённый словарь:")
print(s1)