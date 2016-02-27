# -*- coding: UTF-8 -*-

# A grab bag of scripts and ideas of possible use for basic text mining
# using NLTK

import os, re, nltk
from sys import argv

with open(path_in) as file:
    text = file.read()

    # tokenize / break string into meaningful units, in this case words

    tokens = word_tokenize(text)

    # this separates out punctuation
    tokens = nltk.WordPunctTokenizer().tokenize(s)

    # this pattern strips punctuation
    tokens = nltk.regexp_tokenizer(text, pattern=r'\w+')

    # probably useful helper functions from os library
    # for parsing files/folders

    os.listdir():
    os.mkdir() 
    os.getcwd()

    # frequency distributions

    fdist1 = nltk.FreqDist(tokens)
    top_used = fdist1.most_common(500)
    json.dumps()
