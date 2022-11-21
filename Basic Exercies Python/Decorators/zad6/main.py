def stringer(func):
    def wrapper(*args, **kwargs):
        return str(func(*args, **kwargs))
    return wrapper
