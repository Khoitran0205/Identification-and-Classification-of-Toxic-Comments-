#Tiền xử lý dữ liệu Cranfield**
#Lọc và chỉ lấy các từ
#Tách từ trong câu
#Loại bỏ stopwords
#Sử dụng phương pháp stemma để đưa từ hiện tại về từ gốc của nó
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.snowball import EnglishStemmer
class TextProcessor:
    def __init__(self):
        self.text = ""
        self.text_token = []
    def remove_stopwords(self):
        list_english_stopwords = stopwords.words('english')
        temp  = []
        for item in self.text_token:
            if item not in list_english_stopwords:
                temp.append(item)
        self.text_token = temp            
    def split_words(self):
        self.text_token = word_tokenize(self.text)
    def stemma(self):
        stemmer =  EnglishStemmer()
        self.text_token = [stemmer.stem(word) for word in self.text_token]
        
    def get_only_words(self):
        temp  = []
        self.text = self.text.strip(" ").lower()
        self.text = self.text.split()
        for item in self.text:
            if item.isalpha():
                temp.append(item)
        self.text = " ".join(temp)
    def process(self, text):
        self.text = text
        self.get_only_words()
        self.split_words()
        self.remove_stopwords()
        self.stemma() 
        return self.text_token        


        
    
    