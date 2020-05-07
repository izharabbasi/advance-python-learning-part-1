user_id = ["user1", "user2", "user3"]
names = ["izhar", "sheryar", "ahmed"]

# print(list(zip(user_id, names)))
# print(dict(zip(user_id, names)))

l1 = [1, 2, 3, 4]
l2 = [3, 4, 6, 7]
l = [(1, 2), (3, 4), (5, 6), (7, 8)]
newlist = []


list(zip(*l))

# print(l1)
# print(l2)

for pair in zip(l1, l2):
    newlist.append(min(pair))


print(newlist)
