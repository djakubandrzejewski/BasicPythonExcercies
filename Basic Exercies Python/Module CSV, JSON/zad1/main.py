import csv

with open("wyjscie.csv", mode="w") as plikCSV:
    pola = [key for i in wejscie for key in i.keys()]
    writer = csv.DictWriter(plikCSV, fieldnames=pola)
    pomoc = wejscie
    writer.writeheader()
    for x in pomoc:
        writer.writerow(x)


