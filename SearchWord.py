#coding: utf-8
import twpy
import tweepy
api = twpy.api
query = "ガルパン"

def getTweet(query,limit=100):
    result = []
    for tweet in tweepy.Cursor(api.search,q=query).items(limit):
        result.append(tweet.text)

    # return list of tweets
    return result
