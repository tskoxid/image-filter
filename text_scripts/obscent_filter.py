from csv import reader

PATH_CORPUS: str = r"./data/profane_corpus.csv"
corpus = []
with open(PATH_CORPUS, 'r', encoding='utf8') as f:
    csv_reader = reader(f)
    for row in csv_reader:
        corpus.append(row[0])
corpus: set = set(corpus)


def obscene_filter(input_string, profane_corpus=corpus):
    list_for_check = input_string.split()
    output_str = ''
    for word in list_for_check:
        if word in profane_corpus:
            output_str += word.replace(word, word[0]+(len(word)-1)*'*') + ' '
        else:
            output_str += word + ' '
    return output_str
