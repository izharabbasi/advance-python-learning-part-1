def func(**kwargs):
    for a, b in kwargs.items():
        print(f"{a} : {b}")


d = {"name": "izhar", "age": 20}

func(**d)
