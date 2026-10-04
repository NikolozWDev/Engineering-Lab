import time
import functools
from threading import Lock

def memoize(func):
    cache = {}
    lock = Lock()
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        with lock:
            if key in cache:
                return cache[key]
        result = func(*args, **kwargs)
        with lock:
            cache[key] = result
        return result
    
    wrapper.cache_clear = lambda: cache.clear()
    return wrapper

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            elapsed = time.perf_counter() - start
            print(f"{func.__name__} took {elapsed:.4f}s")
    return wrapper

def validate_types(**expected):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            bound = func.__code__.co_varnames[:func.__code__.co_argcount]
            params = dict(zip(bound, args))
            params.update(kwargs)
            
            for name, typ in expected.items():
                if name in params and not isinstance(params[name], typ):
                    raise TypeError(f"{name} must be {typ.__name__}")
            
            return func(*args, **kwargs)
        return wrapper
    return decorator

def deprecated(reason=""):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            msg = f"{func.__name__} is deprecated"
            if reason:
                msg += f": {reason}"
            print(f"Warning: {msg}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

def singleton(cls):
    instances = {}
    lock = Lock()
    
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instances:
            with lock:
                if cls not in instances:
                    instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    
    return wrapper

if __name__ == "__main__":
    @timer
    @memoize
    def fib(n):
        if n < 2:
            return n
        return fib(n - 1) + fib(n - 2)
    
    print(fib(30))
    
    @validate_types(name=str, age=int)
    def create_user(name, age):
        return {"name": name, "age": age}
    
    print(create_user("Alice", 25))
    
    try:
        create_user("Bob", "old")
    except TypeError as e:
        print(f"Caught: {e}")
    
    @singleton
    class Config:
        def __init__(self):
            self.data = {}
    
    c1 = Config()
    c2 = Config()
    print(c1 is c2)
