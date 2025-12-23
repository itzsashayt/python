while True:
    user_input = input("число: ")

    if user_input.isdigit():
        x = int(user_input)
        result = " ".join(str(i) for i in range(x + 1))
        print(result)
        break
    else:
        print(f"{user_input} - не число. Повторите ввод.")