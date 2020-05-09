def square(a):
    return a**2


l = [1, 2, 3, 4]

# print(list(map(square, l)))


def my_map(func, l):
    new_list = []
    for num in l:
        new_list.append(func(num))
    return new_list


print(my_map(square, l))
