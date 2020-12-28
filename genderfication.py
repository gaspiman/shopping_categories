import os
"""
with open("./data/cross_vertical/luggage.txt") as f:
    lines = f.readlines()
"""

with open("./data/cross_vertical/apparel.txt") as f:
    lines = f.readlines()

cases = [
    ["Men's", "Women's"],
    ["Kids'", "Men's", "Women's"]
]

matches = {
    "Apparel & Accessories > Jewelry > Watches": cases[0],
    "Apparel & Accessories > Clothing": cases[0],
    "Apparel & Accessories > Shoes": cases[0],
    "Luggage & Bags >": cases[1],
}

excludes = [
    "Apparel & Accessories > Clothing > Baby & Toddler Clothing",
    "Luggage & Bags > Luggage Accessories",
    "Luggage & Bags > Handbag & Wallet Accessories"

]

new_lines = []

for line in lines:
    line = line.strip()
    new_lines.append(line+"\n")
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
    for case in matches[found]:
        new_lines.append("{} > {} {}\n".format(line, case, parts[-1]))

with open("./data/cross_vertical/apparel.txt", 'w') as f:
    f.writelines(new_lines)
