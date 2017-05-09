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
import gzip
import pandas as pd

# Cell
# Helper methods provided by the review data source
def parse(path):
    g = gzip.open(path, 'r')
    for l in g:
        yield eval(l)

def getDF(path):
    i = 0
    df = {}
    for d in parse(path):
        df[i] = d
        i += 1
    return pd.DataFrame.from_dict(df, orient='index')

# Cell
df = getDF('reviews_Video_Games_5.json.gz')
df.head()
