def add_sum(*args):
    total = 0
    for num in args:
        total += num
    return total


print(add_sum(1, 2, 3, 4))
