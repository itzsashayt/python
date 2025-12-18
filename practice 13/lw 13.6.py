def exam(text, letter):
    return text.lower().count(letter.lower())

print(exam('My name is Sara.', 's'))