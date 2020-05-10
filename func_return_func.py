def outer_func():
    def innner_func():
        print("this is inner function ")
    return innner_func


var = outer_func()
var()


def outer_func2(msg):
    def innner_func2():
        print(f"Message is {msg}")
    return innner_func2


var1 = outer_func2("Hello There! ")
var1()
