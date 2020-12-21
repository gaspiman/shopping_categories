import os

with open("./data/cross-vertical/luggage.txt") as f:
    lines = f.readlines()

cases = [
    ["Men's", "Women's"],
    ["Kids'", "Men's", "Women's"]
]

matches = {
    "Apparel & Accessories > Jewelry > Watches > ": cases[0],
    "Apparel & Accessories > Clothing >": cases[0],
    "Luggage & Bags >": cases[1],
}

excludes = [
    "Apparel & Accessories > Clothing > Baby & Toddler Clothing",
    "Luggage & Bags > Luggage Accessories",
    "Luggage & Bags > Handbag & Wallet Accessories"

]

for line in lines:
    line = line.strip()
    parts = line.split(" > ")
    found = None
    for m in matches:
        if m in line:
            found = m
            break
    if found is None:
        continue
    for e in excludes:
        if e in line:
            found = None
            break
    if found is None:
        continue
    print(line)
    for case in matches[found]:
        print("{} > {} {}".format(line, case, parts[-1]))
