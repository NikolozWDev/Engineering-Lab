import time
import random
from functools import wraps

def retry(max_attempts=3, delay=1, backoff=2, exceptions=(Exception,)):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 0
            current_delay = delay
            
            while attempt < max_attempts:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    attempt += 1
                    if attempt == max_attempts:
                        raise
                    time.sleep(current_delay + random.uniform(0, 0.1))
                    current_delay *= backoff
            return None
        return wrapper
    return decorator

def rate_limit(max_calls, period):
    calls = []
    
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            now = time.time()
            calls[:] = [c for c in calls if c > now - period]
            
            if len(calls) >= max_calls:
                sleep_time = period - (now - calls[0])
                time.sleep(max(0, sleep_time))
                calls.pop(0)
            
            calls.append(time.time())
            return func(*args, **kwargs)
        return wrapper
    return decorator

def timeout(seconds):
    import signal
    
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            def handler(signum, frame):
                raise TimeoutError(f"Function {func.__name__} timed out after {seconds}s")
            
            old_handler = signal.signal(signal.SIGALRM, handler)
            signal.alarm(seconds)
            
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
                signal.signal(signal.SIGALRM, old_handler)
            
            return result
        return wrapper
    return decorator

if __name__ == "__main__":
    @retry(max_attempts=3, delay=0.5)
    def unstable_function():
        if random.random() < 0.7:
            raise ConnectionError("Connection failed")
        return "Success"
    
    @rate_limit(max_calls=2, period=1)
    def api_call():
        return "API response"
    
    @timeout(2)
    def slow_function():
        time.sleep(5)
        return "Done"
