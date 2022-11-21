b = list(wejscie.values())
newList = []
for i in b:
    if i not in newList:
        newList.append(i)

[print(i) for i in newList]
