# -*- coding: UTF-8 -*-

# A grab bag of scripts and ideas of possible use for basic text mining
# using NLTK

import os, re, nltk
from sys import argv

with open(path_in) as file:
    text = file.read()

    # tokenize / break string into meaningful units, in this case words

    tokens = nltk.word_tokenize(text)

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


for i in os.listdir('.'):
    with open(i) as f:
        text = f.read()
        tokens = nltk.word_tokenize(text)
        fdist = nltk.FreqDist(tokens)
        most_used = fdist.most_common(500)
        path_out = "../freqs/"
        path_out += str.split(i,'.')[0]
        path_out += '.json'
        out = open(path_out,'w')
        out.write(json.dumps(most_used))
        out.close()


