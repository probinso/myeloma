import re
from functools import partial

import nltk
from nltk.stem.snowball import SnowballStemmer

language  = 'english'
stopwords = set(nltk.corpus.stopwords.words(language))
stemmer   = SnowballStemmer(language)
symbolcut = lambda s: re.sub(r'[^\w]', '', s)

from collections import Counter

def tokenize(contents):
    tokens = (word
              for sent in nltk.sent_tokenize(contents)
              for word in nltk.word_tokenize(symbolcut(sent).tolower()))
    return tokens


def process(tokens):
    isnotstop = lambda s: s not in stopwords
    isword    = partial(re.search, '^[A-Za-z]*$')

    stems = filter(isnotstop, map(stemmer.stem, filter(isnotstop, tokens)))
    return stems


def order_vocabulary(collection, threshold = 1):
    vocabulary = Counter()

    for document in collection:
        tokens = tokenize(document)
        vocabulary.update(set(tokens))

    return sorted(counter.items(), key=itemgetter(1), reverse=False)

from Levinshtein import distance as ldist
import numpy as np

def levinshtein_matrix(vocabulary):
    return np.pdist(vocabulary, ldist)
