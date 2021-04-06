from csv import reader

PATH_CORPUS: str = r"../data/profane_corpus.csv"
corpus_list: list = []
with open(PATH_CORPUS, 'r', encoding='utf8') as f:
    csv_reader = reader(f)
    for row in csv_reader:
        corpus_list.append(row[0])
corpus_set: set = set(corpus_list)


class ObscentFilter:
    corpus: set

    def __init__(self, corpus: set):
        self.corpus = corpus

    @staticmethod
    def preprocessing_text(input_text: str):
        input_text = input_text.lower().replace('\n', ' ').replace('\x0c', '')
        input_text = input_text.split(' ')
        filtered_list = []
        for word in input_text:
            filtered_text = [character for character in word if character.isalnum()]
            filtered_list.append("".join(filtered_text))
        return " ".join(filtered_list)

    def filter_text(self, input_string: str):
        list_for_check = input_string.split()
        output_str = ''
        for word in list_for_check:
            if word in self.corpus:
                output_str += word.replace(word, word[0] + (len(word) - 1) * '*') + " "
            else:
                output_str += word + ' '
        return output_str


if __name__ == "__main__":
    text_list = ['Я, БЛЯТЬ, РАЗОЧАРОВАНА, ИДИ НАХУЙ', 'потеряйся нахуй', 'ВСЕ БУДЕТ ТАК, КАК Я ХОЧУ']
    obscent_filter = ObscentFilter(corpus_set)
    for row in text_list:
        text = obscent_filter.preprocessing_text(row)
        print("Строка до фильтра:", row)
        print("Строка после фильтра:", obscent_filter.filter_text(text), '\n')
