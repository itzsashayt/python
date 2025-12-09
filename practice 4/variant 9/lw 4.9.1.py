switch_1 = False
switch_2 = False

answer = input("Включить? ")

if answer.lower() == "да":
    switch_1 = True
    switch_2 = True
    print("Всё включено")
    print(f"switch_1 = {switch_1}, switch_2 = {switch_2}")
else:
    print(f"switch_1 = {switch_1}, switch_2 = {switch_2}")