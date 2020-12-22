import os
from Levenshtein import distance

paths = ["./data/aliexpress.txt", "./data/others/bing_shopping.txt"]
output = "./data/a_to_b.txt"

"""
paths = ["./data/aliexpress.txt", "./data/others/google_shopping.txt"]
output = "./data/a_to_g.txt"
"""

lemmas = {}

with open("./data/lemmatization-en.txt", 'r') as f:
    lines = f.readlines()
    for line in lines:
        parts = line.strip().lower().split()
        lemmas[parts[1]] = parts[0]


def clean_value(value: str):
    value = value.lower()
    value = value.replace("'s", " ")
    value = value.replace("&", " ")
    value = lemmatize(value)
    return value


def lemmatize(s):
    tokens = s.split()
    for i, token in enumerate(tokens):
        tokens[i] = lemmas.get(token, token)
    return " ".join(tokens)


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
            value = clean_value(parts[-1])
            #print("{}|{}|".format(line, value))
            m[line] = value
    maps.append(m)

# fix aliexpress cats:
new_val = {}
for k, v in maps[0].items():
    print(k, v)
    parts = k.split(">")
    if len(parts) < 2:
        continue
    for i in range(len(parts)-1):
        new_key = ">".join(parts[0:i+1]).strip()
        # print("NEW:", new_key, clean_value(parts[i]))
        new_val[new_key] = clean_value(parts[i])
        #print("{}|{}|".format(new_key, clean_value(parts[i])))
        # print(i, clean_value(parts[i]))

for k, v in new_val.items():
    maps[0][k] = v

dist = 0

with open(output, 'w') as f:

    for k, v in maps[0].items():
        for k2, v2 in maps[1].items():
            if v == v2:
                print("{}|{}".format(k, k2))
                f.write("{}|{}\n".format(k, k2))
                continue
            if len(v) > 5 or len(v2) > 5:
                if distance(v, v2) < 2:
                    print("{}|{}".format(k, k2))
                    f.write("{}|{}\n".format(k, k2))
