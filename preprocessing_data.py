#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 10:55:13 2017

@author: sanketh
"""

import json
import pandas as pd
import matplotlib.pyplot as plt

import pickle

path = "/Users/sanketh/Documents/semester2/project_Amanage/del.txt"
tweets_data = []
f = open(path, 'r')
for each in f:
    try:
        tweet = json.loads(each)
        tweets_data.append(tweet)
    except:
        continue
print len(tweets_data)
df = pd.DataFrame()


df['Text'] = map(lambda tweet: tweet['text'] if 'text' in tweet else None, tweets_data)
df['Lang'] = map(lambda tweet: tweet['lang'] if 'lang' in tweet else None, tweets_data)
df['Country_code'] = map(lambda tweet: tweet['place']['country_code'] if 'place' in tweet and 'country_code' in tweet else None, tweets_data)
df['Timestamp'] = map(lambda tweet: tweet['created_at'] if 'created_at' in tweet else None, tweets_data)
df['favorite_count'] = map(lambda tweet: tweet['favorite_count'] if 'favorite_count' in tweet else None, tweets_data)
df['favorited'] = map(lambda tweet: tweet['favorited'] if 'favourited' in tweet else None, tweets_data)
df['retweet_count'] = map(lambda tweet: tweet['retweet_count'] if 'retweet_count' in tweet else None, tweets_data)
df['retweeted'] = map(lambda tweet: tweet['retweeted'] if 'retweet' in tweet else None, tweets_data)


df = df[df.Lang == 'en'] 

pickle.dump(df, open('test', 'wb'))
df.to_csv('test.csv', encoding = 'utf-8')
