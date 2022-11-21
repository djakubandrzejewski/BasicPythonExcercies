class Osoba:
    def __init__(self, imie, nazwisko) -> None:
        self.imie = imie
        self.nazwisko = nazwisko
    def __str__(self) -> str:
        return self.imie +" "+ self.nazwisko
