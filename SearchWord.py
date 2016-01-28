#coding: utf-8
import twpy
import tweepy
api = twpy.api
query = "ガルパン"

# search limit is maybe 200
for tweet in tweepy.Cursor(api.search,q=query).items(100):
    #print(tweet.created_at, tweet.user.screen_name, tweet.text)
    print(tweet.text)

def getTweet(query,limit=100):
    result = []
    for tweet in tweepy.Cursor(api.search,q=query).items(limit):
        result.append(tweet.text)

    # return list of tweets
    return result
