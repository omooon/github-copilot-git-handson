# 0から100までの数字で偶数だけを足す関数
def sum_even_numbers():
    total = 0
    for i in range(2, 101, 2):
        total += i
    return total