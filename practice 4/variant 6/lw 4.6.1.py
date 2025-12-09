text = input("Введите строку: ")
if len(text) > 0:
    print(text[0] == text[-1])
else:
    print(False)