def przywitanie_funkcji(func):
    def wrapper(*args, **kwargs):
        print("Funkcja",func.__name__,"czuję się kochana")
        return func(*args, **kwargs)
    return wrapper
