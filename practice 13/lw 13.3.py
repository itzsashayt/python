def bin_sys(start, end):
    total = 0

    for num in range(start, end + 1):
        binary_num = bin(num)[2:]
        print(binary_num)
        total += num

    binary_total = bin(total)[2:]
    print(f"сумма: {binary_total}")

bin_sys(3, 6)
