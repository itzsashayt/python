def check_password(password):
    if len(password) < 8 or password == "qwerty123":
        return False
    return True

user_input = input("Введите пароль: ")
result = check_password(user_input)
print(result)