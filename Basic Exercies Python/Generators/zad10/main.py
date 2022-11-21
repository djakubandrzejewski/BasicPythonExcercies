import time

def czas():
    start = time.time()
    yield start
    end = time.time()
    yield end
    elapsed_time = end - start
    yield elapsed_time
