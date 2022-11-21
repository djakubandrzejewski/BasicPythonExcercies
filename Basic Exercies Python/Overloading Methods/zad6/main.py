class Osoba:
    def __init__(self, imie, nazwisko) -> None:
        self.imie = imie
        self.nazwisko = nazwisko
    def __del__(self):
        print(self.imie +" "+ self.nazwisko + " umiera")
