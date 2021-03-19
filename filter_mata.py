import pandas as pd


def obscene_filter(path_corpus, input_string):
    profane_corpus = pd.read_csv(path_corpus)
    profane_corpus = set(profane_corpus['Words'])
    list_for_check = input_string.split(' ')
    output_str = ''
    for word in list_for_check:
        if word in profane_corpus:
            output_str += word.replace(word, word[0]+(len(word)-1)*'*') + ' '
        else:
            output_str += word + ' '
    return output_str
