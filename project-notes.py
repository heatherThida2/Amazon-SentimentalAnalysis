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
import pandas as pd

# Cell
# Helper methods provided by the review data source

# Cell
vg = "reviews_Video_Games_5.json"
df = pd.read_json(vg, lines=True)
df.head()
