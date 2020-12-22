from os import listdir
from os.path import isfile, join

input_path = "./data/cross_vertical"
output_file = "./data/cross_vertical.txt"

onlyfiles = [join(input_path, f)
             for f in listdir(input_path) if isfile(join(input_path, f))]

lines = []

for path in onlyfiles:
    print(path)
    file_lines = []
    with open(path) as f:
        for line in f.read().splitlines():
            file_lines.append(line.strip())
    f.close()
    with open(path, 'w') as f:
        file_lines.sort()
        for file_line in file_lines:
            f.write(file_line+"\n")
    f.close()
    lines.extend(file_lines)

lines.sort()

with open(output_file, 'w') as f:
    for line in lines:
        f.write(line+"\n")
