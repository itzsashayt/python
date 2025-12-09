text = input("Введите строку: ")

if len(text) > 0:
    last_char = text[-1].lower()
    if last_char in ["я", "и", "е", "ю"]:
        print(True)
    else:
        print(False)
else:
    print(False)