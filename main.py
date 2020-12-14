import os
from Levenshtein import distance

#paths = ["./data/aliexpress.txt", "./data/bing_shopping.txt"]
#output = "./data/a_to_b.txt"

paths = ["./data/aliexpress.txt", "./data/google_shopping.txt"]
output = "./data/a_to_g.txt"

maps = []


for path in paths:
    print(path)
    m = {}
    with open(path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            parts = line.split(">")
            # print(parts[-1:])
            m[line] = parts[-1]
    maps.append(m)

dist = 0

with open(output, 'w') as f:

    for k, v in maps[0].items():
        for k2, v2 in maps[1].items():
            s = ""
            if v == v2:
                print("{}|{}".format(k, k2))
                f.write("{}|{}\n".format(k, k2))
                continue
            if len(v) > 5 or len(v2) > 5:
                if distance(v, v2) < 2:
                    print("{}|{}".format(k, k2))
                    f.write("{}|{}\n".format(k, k2))
