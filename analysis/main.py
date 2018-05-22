import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
import csv

nltk.download('stopwords')

stopwords = set(stopwords.words("english"))
# nltk.download()
sen = []

with open("C:\\Users\hmgca\Desktop\Coding\inshorts\data\data1.0.csv", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        # print(row[1])
        text = row[1]
        # print(text)
        for w in word_tokenize(text):
            if w not in stopwords:
                sen.append(w)
        print(sen)
        sen = []




