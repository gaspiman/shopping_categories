from os import listdir
from os.path import isfile, join

input_path = "./data/cross-vertical"
output_file = "./data/cross_vertical.txt"

onlyfiles = [join(input_path, f)
             for f in listdir(input_path) if isfile(join(input_path, f))]

lines = []

for path in onlyfiles:
    print(path)
    with open(path) as f:
        for line in f.read().splitlines():
            lines.append(line.strip())

lines.sort()

with open(output_file, 'w') as f:
    for line in lines:
        f.write(line+"\n")
