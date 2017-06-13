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

path = "/Users/sanketh/Documents/semester2/project_Amanage/db_file.txt"
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
df['Text'] = map(lambda tweet: tweet['text'], tweets_data)
df['Lang'] = map(lambda tweet: tweet['lang'], tweets_data)
df['Country_code'] = map(lambda tweet: tweet['place']['country_code'] if tweet['place'] else None, tweets_data)
df['Timestamp'] = map(lambda tweet: tweet['created_at'], tweets_data)
df['favorite_count'] = map(lambda tweet: tweet['favorite_count'], tweets_data)
df['favorited'] = map(lambda tweet: tweet['favorited'], tweets_data)
df['retweet_count'] = map(lambda tweet: tweet['retweet_count'], tweets_data)
df['retweeted'] = map(lambda tweet: tweet['retweeted'], tweets_data)


df = df[df.Lang == 'en']

pickle.dump(df, open('test', 'wb'))
df.to_csv('test.csv', encoding = 'utf-8')
