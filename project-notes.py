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
train2 = train.assign(good = lambda g: g.overall >= 4)
trainFinal = train.assign(good = train2['good'].apply(lambda g: 1 if g else 0))

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
def stem(text):
    stemmer = nltk.stem.porter.PorterStemmer()
    # stem each word individually, and concatenate
    text = ' '.join([stemmer.stem(word) for word in text.split(None)])
    return text

# Cell
def process_text(text):
    text = rm_stopwords_punctuation(text)
    text = stem(text)
    return text

# Cell
trainFinal['reviewText'] = trainFinal['reviewText'].apply(lambda t: process_text(t))

# Cell
test2 = test.assign(good = lambda g: g.overall >= 4)
testFinal = test.assign(good = test2['good'].apply(lambda g: 1 if g else 0))
testFinal['reviewText'] = testFinal['reviewText'].apply(lambda t: process_text(t))

# Cell
y, X = patsy.dmatrices("good ~ reviewText", trainFinal, return_type="dataframe")
y_test, X_test = patsy.dmatrices("good ~ reviewText", testFinal, return_type="dataframe")

### Logistic Regression

# Cell
logRegrModel = skl.linear_model.LogisticRegression()
logRegrModel = logRegrModel.fit(X, y['good'])

# Cell
logRegrModel.score(X, y['good'])

# Cell
logRegrModel.score(X_test, y_test['good'])
