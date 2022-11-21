length = len(wejscie)
with open("wyjscie.txt", 'w') as f:
    for x in range(length):
        f.write(str(wejscie[x]) + "\n")
