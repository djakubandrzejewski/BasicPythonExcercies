def grawitacja_ziemi():
    MASA_ZIEMI = 5,9722 * 10 ** 24
    PROMIEN_ZIEMI = 6373,14
    wynik = 0
    wynik = grawitacja()*(MASA_ZIEMI/PROMIEN_ZIEMI ** 2)
    return wynik
