
def fibonacci_numbers():
    x, y = 0, 1
    while True:
        x, y = y, x+y
        yield x

wyjscie = fibonacci_numbers()


