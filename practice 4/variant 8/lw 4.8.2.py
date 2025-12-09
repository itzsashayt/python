p_c_number = 777

def check_numbers(num1, num2):
    if (num1 < p_c_number and num2 > p_c_number) or (num1 > p_c_number and num2 < p_c_number):
        return True
    return False

n1 = int(input("Введите первое число: "))
n2 = int(input("Введите второе число: "))
result = check_numbers(n1, n2)
print(result)