from csv import reader

PATH_CORPUS: str = r"../data/profane_corpus.csv"
corpus = []
with open(PATH_CORPUS, 'r', encoding='utf8') as f:
    csv_reader = reader(f)
    for row in csv_reader:
        corpus.append(row[0])
corpus = set(corpus)


def preprocessing_text(input_text):
    input_text = input_text.lower().replace('\n', ' ').replace('\x0c', '')
    input_text = input_text.split(' ')
    filtered_list = []
    for word in input_text:
        filtered_text = [character for character in word if character.isalnum()]
        filtered_list.append("".join(filtered_text))
    return " ".join(filtered_list)


def obscene_filter(input_string, profane_corpus=None):
    if profane_corpus is None:
        profane_corpus = corpus
    list_for_check = input_string.split()
    output_str = ''
    for word in list_for_check:
        if word in profane_corpus:
            output_str += word.replace(word, word[0] + (len(word) - 1) * '*') + " "
        else:
            output_str += word + ' '
    return output_str


if __name__ == "__main__":
    text_list = ['Я, БЛЯТЬ, РАЗОЧАРОВАНА, ИДИ НАХУЙ', 'потеряйся нахуй', 'ВСЕ БУДЕТ ТАК, КАК Я ХОЧУ']
    for row in text_list:
        text = preprocessing_text(row)
        print("Строка до фильтра:", row)
        print("Строка после фильтра:", obscene_filter(text), '\n')
