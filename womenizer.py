import os

with open("./data/cross-vertical/apparel.txt") as f:
    lines = f.readlines()

matches = [
    "Apparel & Accessories > Jewelry > Watches > ",
    "Apparel & Accessories > Clothing >",
]

excludes = [
    "Apparel & Accessories > Clothing > Baby & Toddler Clothing"
]

for line in lines:
    line = line.strip()
    parts = line.split(" > ")
    found = False
    for m in matches:
        if m in line:
            found = True
            break
    if found == False:
        continue
    for e in excludes:
        if e in line:
            continue
    print(line)
    print(line + " > Men's " + parts[-1])
    print(line + " > Women's " + parts[-1])
