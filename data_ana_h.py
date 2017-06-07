#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 08:58:14 2017

@author: sanketh
"""

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import datetime


#remove this before final draft
#Currently using Sanketh's account
access_token = "41601603-imMldtIyjNOV4cQs1sVc3t5rpYILR7Ho4BqNkMc8Z"
access_token_secret = "hVBsXq5jjW6jYgHvJELOXLiADTVLLtjLICu51caawjccj"
consumer_key = "IJVQgImqc6hV6w1OLthcaOuMI"
consumer_secret = "s1Zd57mi9OKoA09OWKfaJcahYrcRtxggBpJONfSP2VC9E4FbV6"



class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status

auth = OAuthHandler(consumer_key, consumer_secret)  
auth.set_access_token(access_token, access_token_secret) 
#Below code downloads real time data indefinitely. Need a way to control it
     
if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    print "ok"
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['Apple', 'apple'])
    
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
