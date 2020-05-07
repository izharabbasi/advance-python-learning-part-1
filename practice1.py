
# with simple function


def average_finder(l1, l2):
    average = []
    for pair in zip(l1, l2):
        average.append(sum(pair) / len(pair))
    return average


# with lambda function


lam_average = lambda *args: [sum(pair)/len(pair) for pair in zip(*args)]


print(lam_average([1, 2, 3, 4], [2, 3, 4, 5]))


print(average_finder([1, 2, 3, 4], [2, 3, 4, 5]))
