import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.4f} seconds.")
        return result
    return wrapper

@timer
def heavy_computation(n):
    return sum(i*i for i in range(n))

numbers = [1, 2, 3, 4, 5]
squared_nums = list(map(lambda x: x * x, numbers))
filtered_nums = list(filter(lambda x: x > 10, squared_nums))