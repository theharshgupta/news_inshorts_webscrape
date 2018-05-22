import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
from nltk.tokenize import word_tokenize
import nltk
import csv

asd=[]
index = 0
bjp = 0
modi = 0
india = 0
ipl = 0

tokenList=[]
text = ""

with open("C:\\Users\hmgca\Desktop\Coding\inshorts\out.csv", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        ipl+=1
        text = row[4]
        tokenList += nltk.word_tokenize(text)

        if ipl>100000:
            break

pak = 0
print(tokenList)
# for x in range(0, len(tokenList)):
#     if "BJP" in tokenList:
#         print("found")
#         pak+=1

print(pak)







# for fd in asd:
#     # print(fd + "\n")
#     # if "bjp" or "BJP" or "Bhartiya Janata Party" or "BJP." in fd:
#     #     bjp+=1
#     # if "Modi" or "modi" in fd:
#     #     modi+=1
#     # if "India" in fd:
#     #     india+=1
#     if ("death" in fd) or ("murder" in fd) or ("kill" in fd) or ("killed" in fd) or ("rape" in fd) or ("raped" in fd ):
#
#         pak+=1
#     # if "sIPL" or "ipl" or "Indian Premiere League" in fd:
#     #     ipl+=1
#
# print("Modi in 15 Lakh Articles is: ")
# print(modi)
# print("BJP in the articles is: ")
# print(bjp)
# print("India in the articles is: ")
# print(india)
# print("IPL in the articles is: ")
# print(ipl)
# print("Pakistan in the articles is: ")
# print(pak)
#
#
#
#



