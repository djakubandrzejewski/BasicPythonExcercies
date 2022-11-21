from io import StringIO

def wyjscie(strg):
    file = StringIO(strg)
    file.seek(0)
    file.truncate(100)
    print(file.read())
