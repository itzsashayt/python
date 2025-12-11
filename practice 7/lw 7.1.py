table = [
    ['folder', 'coursework.doc', 'folder', 'pict.png', 'data.accdb'],
    ['icon.ico', 'script.js', 'index.html', 'style.css', 'prog.py'],
    ['my_song.mp3', 'anapa-2003.jpg', 'cs_1.6.exe', 'folder', 'cheat.txt'],
    ['notes.txt', 'main.py', 'work.pdf', 'cartoon.mp4', 'array.py'],
    ['project.psd', 'cycle.py', 'folder', 'cycle.js', 'turtle.py']
]

print("Начальный список")
for row in table:
    print(row)
print()

modified_table = []
for row in table:
    modified_row = []
    for item in row:
        if item != 'folder':
            if item == 'data.accdb':
                modified_row.append('data.sql')
            else:
                modified_row.append(item)
    modified_table.append(modified_row)

print("без папок и с заменой data")
for row in modified_table:
    print(row)
print()

py_files = []
for row in table:
    for item in row:
        if item.endswith('.py'):
            py_files.append(item)

print("Все файлы .py:")
print(py_files)
print()

js_files = []
for row in table:
    for item in row:
        if item.endswith('.js'):
            js_files.append(f"new_{item}")

print("Все new_файлы.js:")
print(js_files)