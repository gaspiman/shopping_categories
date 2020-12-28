# import spacy
import os
import numpy as np
import operator

glove_dir = "/tmp/"


def clean(s):
    s = s.strip()
    s = s.replace("&", "")
    s = s.replace(">", "")
    s = s.replace("'s", "")
    # parts = s.split(" > ")
    # s += " "+parts[-1]
    # s += " "+parts[-1]
    s = " ".join(s.split())

    return s.lower()


def load_glove():
    i = 0
    embedding_index = {}
    f = open(os.path.join('glove.42B.300d.txt'))
    for line in f:
        values = line.split()
        word = values[0]
        coefs = np.asarray(values[1:], dtype='float32')
        embedding_index[word] = coefs
        if i % 1000 == 0:
            print(i)
        i += 1
        """
        if i > 100000:
            break
        """
    f.close()
    return embedding_index


def cosine_similarity(a, b):
    a2 = np.squeeze(np.asarray(a))
    b2 = np.squeeze(np.asarray(b))
    dot = np.dot(a2, b2,  out=None)
    norma = np.linalg.norm(a2)
    normb = np.linalg.norm(b2)
    cos = dot / (norma * normb)
    return cos


freq = {}


def frequencies(paths):
    total = 0.0
    for path in paths:
        with open(path) as f:
            for line in f.readlines():
                line = clean(line)
                for word in line.split():
                    total += 1.0
                    if freq.get(word) is None:
                        freq[word] = 1.0
                    else:
                        freq[word] += 1.0

    for k, v in freq.items():
        freq[k] = 1.0 - (v/total)

    print(freq)


frequencies(["./data/others/aliexpress_fixed.txt",
             "./data/cross_vertical.txt"])


def glove_embed(index, line):
    line = line.strip()
    tokens = line.split()
    avg = np.zeros((1, 300))
    for token in tokens:
        vec = index.get(token, None)
        if vec is None:
            continue
        vec = vec*freq[token]
        avg = avg + vec
    avg = avg / np.linalg.norm(avg)
    # print(avg)
    return avg


print("loading glove...")
glove_index = load_glove()
print(len(glove_index))

"""
print("loading model...")
nlp = spacy.load("en_core_web_md")
"""
m = {}
print("loading building vectors...")
i = 0
with open("./data/cross_vertical.txt") as f:
    lines = f.readlines()
    for line in lines:
        if i % 100 == 0:
            print(i)
        i += 1
        line = line.strip()
        # m[line] = nlp(clean(line))
        m[line] = glove_embed(glove_index, clean(line))


# word = nlp("Automobiles & Motorcycles > Other Vehicle Parts & Accessories > Electric Vehicle Parts > Electric Vehicle Batteries".lower())

"""
word_vector = glove_embed(glove_index, clean(
    "Automobiles & Motorcycles > Other Vehicle Parts & Accessories > Electric Vehicle Parts > Electric Vehicle Batteries"))
"""

# opening aliexpress categorization
with open("./data/alignment/aliexpress.txt", 'w') as ali_f:
    with open("./data/others/aliexpress_fixed.txt") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            word_vector = glove_embed(glove_index, clean(line))
            sims = {}
            for k, v in m.items():
                similarity = cosine_similarity(word_vector, v)
                # print(k, similarity)
                sims[k] = similarity
            sorted_d = dict(
                sorted(sims.items(), key=operator.itemgetter(1), reverse=True))
            count = 0
            s = ""
            for k, v in sorted_d.items():
                if count == 0:
                    print(">>>", line, "|", k, "|", v)
                s += "|" + k + ":" + str(v)
                if count > 1:
                    break
                count += 1
            ali_f.write(line+s+"\n")

exit()
for k, v in m.items():
    similarity = cosine_similarity(word_vector, v)
    print(k, similarity)
    sims[k] = similarity

"""
for k, v in m.items():
    print(k, word.similarity(v))
    sims[k] = word.similarity(v)
"""
sorted_d = dict(
    sorted(sims.items(), key=operator.itemgetter(1), reverse=True))

print("\n>>>>>>\n")
i = 0
for k, v in sorted_d.items():
    print(k, v)
    i += 1
    if i > 5:
        break
