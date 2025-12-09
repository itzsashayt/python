new_message = "Hello! How are you?"
my_response = input("Введите ответ на сообщение: ")

if new_message and my_response:
    print(new_message[0] == my_response[0])
else:
    print(False)