def Constructor(details, people, cars, trees):
    sets_from_details = details // 72
    sets_from_people = people // 4
    sets_from_cars = cars // 2
    sets_from_trees = trees // 7

    return min(sets_from_details, sets_from_people, sets_from_cars, sets_from_trees)

print(Constructor(144, 8, 4, 14))
print(Constructor(10000, 16, 6, 2))