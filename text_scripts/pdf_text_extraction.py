from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import io
import requests


class PdfParser:

    def __init__(self, password='', maxpages: int = 0, caching: bool = True):
        self.rsrcmgr = PDFResourceManager()
        self.retstr = StringIO()
        self.laparams = LAParams()
        self.password = password
        self.maxpages = maxpages
        self.caching = caching
        self.pagenos = set()

    @staticmethod
    def download_pdf(url_pdf: str):
        file = requests.get(url_pdf, stream=True)
        text_bytes = io.BytesIO(file.content)
        return text_bytes

    def convert_pdf_to_txt(self, file):
        device = TextConverter(self.rsrcmgr, self.retstr, laparams=self.laparams)
        interpreter = PDFPageInterpreter(self.rsrcmgr, device)

        for page in PDFPage.get_pages(file, self.pagenos, maxpages=self.maxpages, password=self.password,
                                      caching=self.caching, check_extractable=True):
            interpreter.process_page(page)

        text = self.retstr.getvalue()
        device.close()
        self.retstr.close()
        return text

    @staticmethod
    def text_to_file(data, filename: str):
        with io.open(f'data/{filename}.txt', 'w', encoding='utf8') as file:
            file.write(data)
            file.close()

    def pdf_pipeline(self, filename: str, url: str):
        file = self.download_pdf(url)
        text = self.convert_pdf_to_txt(file)
        text = text.replace('-\n', '')
        self.text_to_file(text, filename)
        return text


if __name__ == "__main__":
    URL_PDF = [r'https://arxiv.org/pdf/1909.11687.pdf']
    parser = PdfParser()
    count = 0
    for URL in URL_PDF:
        paper = parser.pdf_pipeline(f'file_{count}', URL)
        count += 1
        print(paper)