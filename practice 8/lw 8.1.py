my_dict = {1:'0101101', 2:'101110', 3:'1A14C', 4:'1100100', 5:'101010'}
print("Исходный словарь:")
print(my_dict)


my_dict.pop(3)
print("После удаления ключа 3:")
print(my_dict)


my_dict[10] = '0100101'
print("После добавления ключа 10:")
print(my_dict)