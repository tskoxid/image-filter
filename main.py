import pytesseract
from PIL import ImageFile
from csv import reader
from image_scripts.classes import ImageClassification
from text_scripts.obscent_filter import ObscentFilter
import time
import tarfile


PATH_TESSERACT: str = r'C:\Users\Artem\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
PATH_TESSERACT_LINUX: str = r'/usr/bin/tesseract'
PATH_CORPUS: str = r".\data\profane_corpus.csv"
pytesseract.pytesseract.tesseract_cmd = PATH_TESSERACT
ImageFile.LOAD_TRUNCATED_IMAGES = True

tar = tarfile.open("data/models.tar.gz")
tar.extractall("data/")
tar.close()

corpus_list: list = []
with open(PATH_CORPUS, 'r', encoding='utf8') as f:
    csv_reader = reader(f)
    for row in csv_reader:
        corpus_list.append(row[0])
corpus_set: set = set(corpus_list)


def main(cls, url_image: str):
    result = cls.pipline_filter(url_image)
    return result


if __name__ == '__main__':
    url_image_list = ['https://i.pinimg.com/564x/ff/12/c4/ff12c41417f4d15220628479754ede42.jpg',
                      'https://i.pinimg.com/564x/0b/76/24/0b7624609162e8336908df59231735c5.jpg',
                      'https://i.pinimg.com/564x/ef/25/22/ef2522bab80dc1f9291d1c159a346ce1.jpg',
                      'https://i.redd.it/pk7p8xa8hph11.jpg',
                      'https://i.imgur.com/0NLsRgl.jpg',
                      'https://i.redd.it/jlwxg2i4rbn11.jpg',
                      'https://i.imgur.com/iIFS0GW.jpg',
                      'https://i.imgur.com/all7awG.jpg',
                      'https://i.redd.it/0h10sajru6s11.jpg',
                      'https://i.redd.it/q4r1lnkom1k11.jpg',
                      'http://i.imgur.com/FvoPXwV.jpg',
                      'https://i.redd.it/easnunqwgri01.jpg',
                      'https://i.imgur.com/O3pq4dH.jpg',
                      'https://i.redd.it/c1r4p1au26t01.jpg',
                      'https://i.redd.it/sjrhm72wn1i11.jpg']

    start_time = time.time()

    new_examaple = ImageClassification(corpus_set, model_path=r'data/models')

    print(f"Init model {time.time()-start_time} секунд")

    for URL_IMAGE in url_image_list:
        start_time = time.time()
        main(new_examaple, URL_IMAGE)
        print(time.time() - start_time, '\n')

    text_list = ['Я, БЛЯТЬ, РАЗОЧАРОВАНА, ИДИ НАХУЙ', 'потеряйся нахуй', 'ВСЕ БУДЕТ ТАК, КАК Я ХОЧУ', 'ПошёЛ ,НахУй']
    obscent_filter = ObscentFilter(corpus_set)

    for row in text_list:
        text_row = obscent_filter.obscene_filter(row)
        print("Строка до фильтра:", row)
        print("Строка после фильтра:", obscent_filter.obscene_filter(text_row), '\n')
