# A simple generator function
def N():
    i = 0
    while True:
        yield i
        i += 1
