import csv
pomoc = []
suma = 0
with open('proba.csv', 'r') as plikCSV:
    czytnikCSV = csv.reader(plikCSV, delimiter="\t")
    wiersze = [wiersz for wiersz in czytnikCSV]
    for row in wiersze:
        for item in row:
            pomoc.append(item)
        lipton = [float(x) for x in pomoc]
        suma = sum(lipton)
        dlugosc = len(lipton)
        srednia = suma / dlugosc
        print(srednia)
