my_dict = {}
while len(my_dict) < 3:
    try:
        key = int(input("Введите ключ (число): "))
    except ValueError:
        print("Ключ должен быть число!")
        continue
    
    value = input("Введите зачения: ")
    my_dict[key] = value
    print(f"Текущий словарь {my_dict}")
    
    print("Словарь заполнен:", my_dict)