text = input("Введите строку: ")
length = len(text)

if length == 0:
    print(None)
elif length <= 5:
    print("short")
elif 6 <= length <= 10:
    print("normal")
else:
    print("long")