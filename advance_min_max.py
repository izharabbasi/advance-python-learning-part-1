names = ["izhar", "sheryar", "ahmed"]

# print(max(names, key=lambda item: len(item)))


players = [
    {"name": "izhar", "score": 90, "age": 20},
    {"name": "sheryar", "score": 80, "age": 21},
    {"name": "ahmed", "score": 60, "age": 25}
]


print(max(players, key=lambda item: item.get("age"))['name'])
