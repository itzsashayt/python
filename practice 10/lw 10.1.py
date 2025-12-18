def upper(t):
    result = ""
    for char in t:
        if char.isupper():
            result += char + " "
    return result.strip()
print(upper("PriVet"))