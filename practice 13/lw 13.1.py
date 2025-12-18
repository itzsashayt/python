def alpha(user_string):
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    
    print(alphabet)
    
    used_letters = ""
    unused_letters = ""
    
    for letter in alphabet:
        if letter in user_string:
            used_letters += letter
        else:
            unused_letters += letter
    
    result = used_letters + unused_letters
    print(result)
    
    return result

alpha('пайтон')