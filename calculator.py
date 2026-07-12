# 0から100までの数字で奇数だけを足す関数
def sum_odd_numbers():
    total = 0
    for i in range(1, 101, 2):
        total += i
    return total