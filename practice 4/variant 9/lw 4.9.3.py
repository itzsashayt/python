text = input("Введите строку: ")

if text and text[0] == "/":
    print("command")
else:
    print("It's string")