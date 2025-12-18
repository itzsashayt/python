def punct(txt):
    signs = "!?.,()"
    count = 0
    for char in txt:
        if char in signs:
            count += 1
    return count
print(punct("(Как дела?)"))