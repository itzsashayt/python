mass = [14, -6, 3, 11, 6, 8.5, 99, -20, -6, 10, 40, 0.25, -4, 5]

for num in mass.copy():
    if num < 0:
        mass.remove(num)

        sorted_asc = sorted(mass)
        print(sorted_asc)

        sorted_desc = sorted(mass, reverse=True)
        print(sorted_desc)