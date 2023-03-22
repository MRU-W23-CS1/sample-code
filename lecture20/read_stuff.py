f = open("data/stuff.txt", "r")
stuff = []
for line in f:
    stuff.append(line)
f.close()
print(stuff)