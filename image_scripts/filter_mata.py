from csv import reader
import os

PATH_CORPUS: str = r"./data/profane_corpus.csv"

corpus = []
with open(PATH_CORPUS, 'r', encoding='utf8') as f:
    csv_reader = reader(f)
    for row in csv_reader:
        corpus.append(row[0])
corpus: set = set(corpus)


def obscene_filter(input_string, profane_corpus=corpus):
    list_for_check = input_string.split(' ')
    for word in list_for_check:
        if word in profane_corpus:
            return False
        else:
            continue
    return True
