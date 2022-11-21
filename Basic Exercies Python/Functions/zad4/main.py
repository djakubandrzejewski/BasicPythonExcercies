import math


def d(x, y, z = 0):
    xb = (0 - x)**2
    yb = (0 - y)**2
    zb = (0 - z)**2
    wynik = math.sqrt(xb+yb+zb)
    return wynik

