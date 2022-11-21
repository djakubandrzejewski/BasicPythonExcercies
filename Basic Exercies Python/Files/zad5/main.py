f1 = open("wyjscie.txt", "w")

with open("wejscie.txt", "r") as myfile:
    data = myfile.read()
data_1 = data[::-1]
f1.write(data_1)
f1.close()
