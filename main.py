def print_num_gt(num):
    def decorator(func):
        def wrapper(x):
            if x > num:
                result = func(x)
            else:
                print("error")
                result = None
            return result
        return wrapper
    return decorator

@print_num_gt(3)
def print_num(x: int):
    print(x)
    
print_num(3)