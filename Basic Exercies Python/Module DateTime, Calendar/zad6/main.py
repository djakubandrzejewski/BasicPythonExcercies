from datetime import date
sorted_values = sorted(wejscie.values())
sorted_dict = {}
for i in sorted_values:
    for k in wejscie.keys():
        if wejscie[k] == i:
            sorted_dict[k] = wejscie[k]
wyjscie = list(sorted_dict.keys())


