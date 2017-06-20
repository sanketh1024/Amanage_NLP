#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 17:35:43 2017

@author: sanketh
"""

#sentiment analysis

from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize
from nltk import word_tokenize, pos_tag, ne_chunk

import pickle
from textblob import TextBlob
import pandas as pd

import re
sid = SentimentIntensityAnalyzer()

sent = ["This is a bad example", "Quarter 4 results are bad", "Elections are rigged :)", "Apple headphone is very "]

#n_instances = 100
#subj_docs = [(sent, 'subj') for sent in subjectivity.sents(categories='subj')[:n_instances]]
#obj_docs = [(sent, 'obj') for sent in subjectivity.sents(categories='obj')[:n_instances]]
#for sent in subjectivity.sents(categories='subj')[:n_instances]:
#    print sent
#    break

#first tokanizer


def ner(tweet):
    return ne_chunk(pos_tag(word_tokenize(tweet)))
    
def scoring_vader(tweet):
    ss = sid.polarity_scores(tweet)
    l = []
    for k in sorted(ss):
            l.append('{0}: {1}, '.format(k, ss[k]))
    return l, ss['compound']
def scoring_g2g(tweet):
    analysis = TextBlob(tweet)
    return analysis.sentiment.polarity

def clean_tweet(tweet):
        '''
        Utility function to clean tweet text by removing links, special characters
        using simple regex statements.
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
df = pickle.load(open('test', 'rb'))
df['preprocessed_tweet'] = df['Text'].apply(clean_tweet)

df['NER'] = df['preprocessed_tweet'].apply(ner)
df['tweet_score_vader'] = df['preprocessed_tweet'].apply(scoring_vader)
df['tweet_score_g2g'] = df['preprocessed_tweet'].apply(scoring_g2g)
#print df
print len(df)
df = df.drop_duplicates(subset = ['Text'])
print len(df)
df1 = df['preprocessed_tweet'].apply(lambda x: x.replace('RT ', ''))
df1 = df1.drop_duplicates().reset_index(drop = True)
df1.to_csv('scoring.csv', encoding = 'utf-8')
print "Total score vader", sum(score[1] for score in df['tweet_score_vader'])
print "Total score g2g", df['tweet_score_g2g'].sum()

#for sentence in sent:
#    print(sentence)
#    ss = sid.polarity_scores(sentence)
#    for k in sorted(ss):
#        print ('{0}: {1}, '.format(k, ss[k]))
#    print()
    
#second tokanizer

#from nltk.tokenize import TweetTokenizer
#
#tze = TweetTokenizer(strip_handles =True, reduce_len = True)
#l = []
#for s in sent:
#    l.append(tze.tokenize(s))
#print l