

# position = 0

# for name in names:
#     print(f"{position} --> {name}")
#     position += 1


# for position, name in enumerate(names):
#     print(f"{position} --> {name}")

names = ["izhar", "shery", "umair"]


def find(l, finder):
    for pos, name in enumerate(l):
        if name == finder:
            return f"{name} {pos}"
        else:
            return -1


print(find(names, "izhar"))
