def custom_filter(lst):
    total = 0
    for item in lst:
        if isinstance(item, int) and item % 7 == 0:
            total += item
    print(f"сумма: {total}")
    return total <= 83

print(custom_filter([1, 10.5, 'txt', 14, 2, 56]))