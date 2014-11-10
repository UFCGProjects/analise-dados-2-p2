def append(dic, term, title):
    # if term not in dic:
    #     dic[term] = {}

    for word in title.split(" "):
        word = unnacent(word)

        if len(word) < 4:
            continue

        if word not in dic:
            dic[word] = [0, 0, 0, 0, 0, 0]

        if (term == "rock"):
            dic[word][0] += 1
        elif (term == "jazz"):
            dic[word][1] += 1
        elif (term == "alternative rock"):
            dic[word][2] += 1
        elif (term == "electronic"):
            dic[word][3] += 1
        elif (term == "pop"):
            dic[word][4] += 1

def save(dic):
    csvOutput = open("csv/term_word_count.csv", "w")

    csvOutput.write("word,rock,jazz,alternative rock,eletronic,pop,total\n")

    for word in dic:
        csvOutput.write("%s,%d,%d,%d,%d,%d,%d\n" % (word, dic[word][0], dic[word][1], dic[word][2], dic[word][3], dic[word][4], sum(dic[word])))

    csvOutput.close()

def unnacent(word):
    i = 0

    while (i < len(word)):
        c = word[i]

        if (c.isalpha()):
            i += 1
        else:
            word = word.replace(c, "")
            i = 0

    return word


def main():
    csvInput = open("csv/term_title.csv", "r")

    dic = {}
    i = 0

    for line in csvInput.read().replace("\"", "").split("\n"):
        values = line.split(",")

        if (len(values) > 1):
            append(dic, values[1], values[2])

    csvInput.close()

    save(dic)

if __name__ == "__main__":
    main()