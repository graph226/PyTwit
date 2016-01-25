#coding:utf-8
# importing Tweepy library
import tweepy

#setting my keys
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""
auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)

#creating api instance
api = tweepy.API(auth)

print("ok!")
