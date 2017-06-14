#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 08:58:14 2017

@author: sanketh
"""

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import tweepy
import datetime
import sys

#remove this before final draft
#Currently using iGenie's account
access_token = "872339058227384321-n5XtDqYSFctW6zwbCxFwmCeQWLuXRRP"
access_token_secret = "1lCeWKmXb54hdh3AM22teSmpAxkTjK77dJ0M5mIhaOkCb"
consumer_key = "kY60GVaF6EsFkKKAxmGJmZFhw"
consumer_secret = "cRpZHZrzVxPhAGak17uHKIQpOXYq0wxiczq7beebmxiN2YTzs7"

print sys.argv
class StdOutListener(StreamListener):
    def __init__(self, lim = 20):
        self.num_tweets = 0
        self.lim = lim
        self.file = open(str(sys.argv[2]), 'w')
    def on_data(self, data):
        while self.num_tweets < self.lim:
            self.file.write(data)
            self.num_tweets += 1
            print self.num_tweets
            return True
        return False

    def on_error(self, status):
        pass
        #print status

auth = OAuthHandler(consumer_key, consumer_secret)  
auth.set_access_token(access_token, access_token_secret) 
#Below code downloads real time data indefinitely. Need a way to control it
     
if __name__ == '__main__':
    #This handles Twitter authetification and the connection to Twitter Streaming API
    print sys.argv[1]
    l = StdOutListener(int(sys.argv[1]))
    print "ok"
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    while True:
        try:
            stream.filter(track=[str(sys.argv[3])])
            break
        except tweepy.TweepError:
            pass

    
# Below code downloads data for the start and end dates specified
#def date_range(start,end):
#   current = start
#   while (end - current).days >= 0:
#      yield current
#      current = current + datetime.timedelta(seconds=1)  
#   
#class TweetListener(StreamListener):
#    def on_status(self, status):
#        #api = tweepy.API(auth_handler=auth)
#        #status.created_at += timedelta(hours=900)
#
#        startDate = datetime.datetime(2017, 04, 30)
#        stopDate = datetime.datetime(2017, 05, 30)
#        for date in date_range(startDate,stopDate):
#            status.created_at = date
##            print "tweet " + str(status.created_at) +"\n"
##            print (status.text + "\n").encode('utf-8')  
#            print status
            # You can dump your tweets into Json File, or load it to your database

#stream = Stream(auth, TweetListener(), secure=True, )
#stream.filter(track=[u'Apple', u'apple'])
    

#IJVQgImqc6hV6w1OLthcaOuMI    API key
#s1Zd57mi9OKoA09OWKfaJcahYrcRtxggBpJONfSP2VC9E4FbV6    API secret
#41601603-imMldtIyjNOV4cQs1sVc3t5rpYILR7Ho4BqNkMc8Z   access token
#hVBsXq5jjW6jYgHvJELOXLiADTVLLtjLICu51caawjccj     access token secret
