def add_sum(*args):
    if all([(type(arg) == int or type(arg) == float) for arg in args]):
        total = 0
        for num in args:
            total += num
        return total
    else:
        return "Please enter numbers"
        
        


print(add_sum(1, 2, 3, 4,"asa"))
