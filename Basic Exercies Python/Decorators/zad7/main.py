def bezbledny(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except:
            print("Funkcja",func.__name__,"wywołała błąd, ale jest jej bardzo przykro")
    return wrapper
