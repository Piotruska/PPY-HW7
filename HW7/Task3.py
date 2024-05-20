import time

def time_execution(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} s")
        return result
    return wrapper

@time_execution
def example_function():
    time.sleep(1)
    return "Executed After 1 Second"