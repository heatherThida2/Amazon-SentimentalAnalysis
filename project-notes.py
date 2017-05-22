"""
Amazon Review Data

CSCI 183
Spring 2017
Final Project
Prof. Manna

Thida Aung, Sanjay Kaliyur, Erik Trewitt

Process for working with our data; will later be transformed into a
jupyter notebook.
"""

# Cell
import json
import nltk # stemmer
import numpy as np
import pandas as pd
import re
import sklearn as skl
import string

# Cell
train = pd.read_json("data/music_200.json", lines=True)
test = pd.read_json("data/music_test_200.json", lines=True)
train.head()

# Cell
train = train.drop(['asin', 'helpful', 'reviewTime', 'reviewerID', 'reviewerName', 'summary', 'unixReviewTime'], axis=1)
test = test.drop(['asin', 'helpful', 'reviewTime', 'reviewerID', 'reviewerName', 'summary', 'unixReviewTime'], axis=1)
train.head()

# Cell
# train.assign(good = lambda g: g.overall >= 4)
# train.assign(good = lambda g: (1, 0)[g.overall >= 4])
train2 = train.assign(good = lambda g: g.overall >= 4)
train.assign(good = train2['good'].apply(lambda g: 1 if g else 0))

# Cell
def rm_stopwords_punctuation(text):
    text = text.lower()
    with open("stopwords.json") as stopword_file:
        stopwords = json.load(stopword_file)
        for word in stopwords:
            if word in text:
                # replace only complete words ('\b' is a word boundary)
                text = re.sub(r"\b{}\b".format(word), "", text)
    # remove punctuation
    for char in string.punctuation:
        text = text.replace(char, "")
    text = re.sub(r"\b[a-z]\b", "", text)
    # remove whitespace
    for char in string.punctuation:
        text = text.replace(char, "")
    text = ' '.join(text.split(None))
    return text

# Cell
for text in train2['reviewText']:
    text = rm_stopwords_punctuation(text)

# Cell
train3 = train2.copy()
train3['reviewText'] = train2['reviewText'].apply(lambda t: rm_stopwords_punctuation(t))

# Cell
train2['reviewText']
