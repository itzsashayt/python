path = "C:\\Users\\MainAdmin\\Desktop\\programs"
print(f"1. Начальное значение переменной path: {path}")
print(f"2. Вывод значения path: {path}")
path += "\\game.exe"
print(f"3. Добавлена строка '\\game.exe'")
print(f"4. Измененное значение path (путь к файлу): {path}")
path = "C:\\Users\\MainAdmin\\Desktop\\files"
print(f"5. Значение path изменено на: {path}")
path += "\\picture.png"
print(f"6. Добавлена строка '\\picture.png'")
print(f"7. Измененное значение path (путь к изображению): {path}")
path = "C:\\Games\\city simulator"
print(f"8. Значение path изменено на: {path}")
path *= 2
print(f"9. 'Ошибочный' путь (значение path умножено на 2): {path}")
print("   Примечание: умножение строки на число повторяет ее содержимое, что не является стандартным способом обработки путей.")
print(f"10. Error path: {path}")
print("   Примечание: умножение строки на число повторяет ее содержимое, что не является стандартным способом обработки путей.")