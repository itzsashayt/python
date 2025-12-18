def square(x, y):
    print("_" * (4 * y + 1))
    
    for i in range(x):
        row = "|"
        for j in range(1, y + 1):
            row += f" {j} |"
        print(row)
    
    print("_" * (4 * y + 1))

square(2, 3)