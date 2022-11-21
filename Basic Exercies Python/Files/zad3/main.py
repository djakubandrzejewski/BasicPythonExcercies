total = 0
with open("wejscie.txt", 'r') as f:
    for x in f:
        x = x.strip()
        nums = x.split("\n")
        for ns in nums:
            total = total + int(ns)

print(total)

