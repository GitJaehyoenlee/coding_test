import time
from functools import wraps

def spend_time(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = fn(*args, **kwargs)
        end_time = time.time()
        print(f"Spend Time [{fn.__name__}]: {end_time - start_time} sec")
        return result
    return wrapper