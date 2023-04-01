from public.fibonacci import F as fibo
from time import perf_counter

# Timer decorator

def timer(fn):
    from time import perf_counter
    
    def inner(*args, **kwargs):
        start_time = perf_counter()
        to_execute = fn(*args, **kwargs)
        end_time = perf_counter()
        execution_time = end_time - start_time
        print("\nExecution with input {0:d} took {1:.8f}s to execute".format(args[0], execution_time))
        return to_execute
    
    return inner

@timer
def decorated_fibo(n):
    fibo(n)
    
def test_with_one():
    decorated_fibo(1)

def test_with_ten():
    decorated_fibo(10)

def test_with_twenty():
    decorated_fibo(20)

def test_with_thirty():
    decorated_fibo(30)

def test_with_thirty_one():
    decorated_fibo(31)

def test_with_thirty_two():
    decorated_fibo(32)

# Do not try this at home!    
# def test_with_fourty():
    # fibo(40)
    
# Do not try this at home!
# def test_with_fifty():
#     fibo(50)
