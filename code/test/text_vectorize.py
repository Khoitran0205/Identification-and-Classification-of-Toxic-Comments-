import pickle as pk
import numpy as np
class TextVectorizer:
    def __init__(self):
        self.text_vectorizer = []
        self.text_token =  []
        self.dict_bad_words = {}
        self.dict_good_words = {}
    dict_toxic_positive_vector_each_sentence = {}
    def count_vector_positive(self,positive):
        arr  =  []
        for item in positive:
            arr.append(self.dict_good_words[item])
        if (len(arr)  ==  0):
            return np.full(50, 0.0)
        else:
            arr = np.sum(arr, axis = 0)
            return np.dot(len(positive) ,arr)
    def toxic_positive_words(self):
        positive = [word for word in self.text_token if word in self.dict_good_words]
        toxic = [word for word in self.text_token if word in self.dict_bad_words]
        return positive, toxic
    def count_vector_toxic(self,toxic):
        arr  = []
        for item in toxic:
            arr.append(self.dict_bad_words[item])
        if (len(arr)  ==  0):
            return np.full(50, 0.0)
        else:
            arr = np.sum(arr, axis = 0)
            return np.dot(len(toxic) ,arr)
    def count_vectorizer(self):
        positive, toxic  = self.toxic_positive_words()
        return np.sum([self.count_vector_positive(positive) ,self.count_vector_toxic(toxic)], axis =0)
        
    def process(self, text_token):
        self.text_token = text_token
        self.dict_good_words = pk.load(open('D:/Identification-and-Classification-of-Toxic-Comments-/code/dict_positive_words.pkl', 'rb'))
        self.dict_bad_words = pk.load(open('D:/Identification-and-Classification-of-Toxic-Comments-/code/dict_bad_words.pkl', 'rb'))
        return self.count_vectorizer()

