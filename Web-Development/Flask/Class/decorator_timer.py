import time

def timer(func): # args= name: int, number
    def wrapper(*args, **kwargs):
        start = time.perf_counter_ns()
        result = func(*args, **kwargs)
        delta = time.perf_counter_ns() - start
        print(f"Function: {func.__name__}  [{delta:,.5f} ns]")
        return result
    return wrapper

@timer
def factorial(n: int) -> int:
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    n = 10
    fact = factorial(n)
    print(f"{n}! = {fact}")