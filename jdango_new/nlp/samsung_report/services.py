
import nltk
from nlp.samsung_report.models import Entity, SamsungService


class Controller:
    def __init__(self):
        self.entity = Entity()
        self.service = SamsungService()

    def download_dictionary(self):
        nltk.download('punkt')

    def data_analysis(self):
        self.download_dictionary()
        self.entity.fname = 'kr-Report_2018.txt'
        self.entity.context = 'C:\\Users\\AIA\\project\\jdango_new\\nlp\\samsung_report\\data\\'
        self.service.extract_tokens(self.entity)
        self.service.extract_hangeul()
        self.service.conversion_token()
        self.service.compound_noun()
        self.entity.fname = 'stopwords.txt'
        self.service.extract_stopword(self.entity)
        self.service.filtering_text_with_stopword()
        data = self.service.frequent_text()
        self.entity.fname = 'D2Coding.ttf'
        self.service.draw_wordcloud(self.entity)
        return data
    def test(self):
        self.download_dictionary()
        self.entity.fname = 'kr-Report_2018.txt'
        self.entity.context = 'C:\\Users\\AIA\\project\\jdango_new\\nlp\\samsung_report\\data\\'
        self.service.extract_tokens(self.entity)
        self.service.extract_hangeul()
        self.service.conversion_token()
        self.service.compound_noun()
        self.entity.fname = 'stopwords.txt'
        self.service.extract_stopword(self.entity)
        self.service.filtering_text_with_stopword()
        data= self.service.frequent_text()
        return data

if __name__ == '__main__':

    app = Controller()
    app.data_analysis()
