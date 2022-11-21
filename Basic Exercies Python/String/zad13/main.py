import string 
h = input()
x = 0

for i in h:
    if i in string.whitespace:
        x += 1
if(x > 0):
    print("TAK")
else:
    print("NIE")
