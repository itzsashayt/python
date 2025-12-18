def begin(field, row, col):
    field[row][col] = '*'

    for r in range(3):
        row_str = ""
        for c in range(3):
            row_str += field[r][c] + " "
        print(row_str.strip())

field = [['[]', '[]', '[]'],
         ['[]', '[]', '[]'],
         ['[]', '[]', '[]']]

begin(field, 1, 2)