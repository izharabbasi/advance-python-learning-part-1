def outer_func():
    def innner_func():
        print("this is inner function ")
    return innner_func


var = outer_func()
var()
