import logging
import sys

def log(filename=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if filename:
                logging.basicConfig(filename=filename, level=logging.INFO)
            else:
                logging.basicConfig(stream=sys.stdout, level=logging.INFO)

            try:
                result = func(*args, **kwargs)
                logging.info(f'{func.__name__} ok')
                return result
            except Exception as e:
                logging.error(f'{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}')
                raise e

        return wrapper
    return decorator




@log(filename=None)
def summa(x, y):
    return x + y
z = summa(35, 4)
print(z)