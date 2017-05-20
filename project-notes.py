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
import numpy as np
import pandas as pd
import sklearn as skl

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
    with read("stopwords.json") as stopwords:
        for word in stopwords:
            text.replace(word, "")
    # TODO: remove punctuation
    return text
