numbers = [1, 2, 3, 4, 5, 6]

sqaure = map(lambda a: a**2, numbers)
# this is called iterator
print(sqaure)
print(next(sqaure))
print(next(sqaure))
print(next(sqaure))
print(next(sqaure))

# this is called iterables

for i in numbers:
    if i % 2 == 0:
        print(i)
