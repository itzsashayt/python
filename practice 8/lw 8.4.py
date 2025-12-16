a11_d = {1: 15, 4: 80, 44: 0, 256: 15, 100: 70, 101: 70, 20: 44, 3: 9}
keys_to_remove = [1, 101, 3]

for key in keys_to_remove:
    a11_d.pop(key, None)
    
print("Словарь ппосле удаления:")
print(a11_d)