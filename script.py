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

def writeterm(csv, term, i):

    csv.write(term)

    total = 0

    for word in dic:
        total += dic[word][i]
        csv.write(";%d" % dic[word][i])

    csv.write(";%d\n" % total)

def save(dic):
    csvOutput = open("csv/term_word_count.csv", "w")

    csvOutput.write("word,rock,jazz,alternative rock,electronic,pop,total\n")

    for word in dic:
        total =  float(sum(dic[word]))

        r = ("%s,%f,%f,%f,%f,%f,%f\n" % (word, dic[word][0], dic[word][1], dic[word][2], dic[word][3], dic[word][4], total))
        csvOutput.write(r)

    # csvOutput2 = open("csv/term_word_count.csv", "w")

    # csvOutput2.write("term");

    # for word in dic:
    #     csvOutput2.write(";%s" % word)

    # csvOutput2.write(";total\n")

    # writeterm(csvOutput2, "rock", 0)
    # writeterm(csvOutput2, "jazz",1)
    # writeterm(csvOutput2, "alternative rock", 2)
    # writeterm(csvOutput2, "electronic", 3)
    # writeterm(csvOutput2, "pop", 4)



    # for word in dic:
    #     csvOutput.write("%s,%d,%d,%d,%d,%d,%d\n" % (word, dic[word][0], dic[word][1], dic[word][2], dic[word][3], dic[word][4], sum(dic[word])))


    # csvOutput.close()

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

dic = {}

def main():
    csvInput = open("csv/term_title.csv", "r")

    i = 0

    for line in csvInput.read().replace("\"", "").split("\n"):
        values = line.split(",")

        if (len(values) > 1):
            append(dic, values[1], values[2])

    csvInput.close()

    save(dic)

if __name__ == "__main__":
    main()
