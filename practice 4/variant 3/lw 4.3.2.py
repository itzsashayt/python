filename = input("Введите имя файла с расширением: ")
extension = filename.split('.')[-1].lower()

if extension == 'doc':
    print("Word file")
elif extension == 'py':
    print("Python file")
elif extension == 'txt':
    print("Text file")
else:
    print("Неизвестное расширение")