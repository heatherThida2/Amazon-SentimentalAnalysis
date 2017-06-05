# CSCI 183 Final Project

**Logistic Regression & Naive Bayes on Amazon review data**

*Thida Aung, Sanjay Kaliyur, Erik Trewitt*

Jupyter Notebook with a Python 3.5.2 kernel.

***

### Setup instructions

0. Clone this project using `git clone git@github.com:sanjaykaliyur/CSCI183-Project.git`.

1. If you don't already have it, install Python 3.5+ from [python.org](https://www.python.org/downloads/) or using `sudo apt-get install python3`.

2. Install pip3:
 * Unix: `sudo apt-get install python3-pip`.
 * Other: Follow [pip's manual installation instructions](https://pip.pypa.io/en/stable/installing/).

3. Make sure your version of pip is up to date using `pip3 install --upgrade pip`.

4. Install Jupyter using `pip3 install jupyter`.

5. Install required dependencies using `pip3 install $(cat install-requires.txt)`.

6. Extract the compressed data files: cd tar -xvf data.tar.gz

7. Open the project notebook:  
`python3 -m jupyter notebook sentiment-analysis--amazon_commented.ipynb`.

***

### External Dependencies:

- `matplotlib`: Data plotting tool
- `nltk`: Natural language toolkit, used for stemming
- `pandas`: Data processing toolkits
- `sklearn`: Machine learning algorithm library
