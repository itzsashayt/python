lamp_1 = 0
lamp_2 = 0

print("Какую лампочку зажечь?")
answer = input("Введите '1' или '2': ")

if answer == "1":
    lamp_1 = 1
    print(f"Лампочка 1 зажжена. Состояние: lamp_1={lamp_1}, lamp_2={lamp_2}")
elif answer == "2":
    lamp_2 = 1
    print(f"Лампочка 2 зажжена. Состояние: lamp_1={lamp_1}, lamp_2={lamp_2}")
else:
    print("Обе лампочки не горят")