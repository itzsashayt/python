m = ['круг', 0.25, 'квадрат', 'треугольник', 15, 'круг', 'овал', '10']

for item in m.copy():
    if not isinstance(item, str):
        m.remove(item)

print(m)