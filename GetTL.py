#importing modules
import twpy
import tweepy

api = twpy.api

print ("how many tweets do you want to retrieve?"),
#count = int(input())
count = 1000

result = []
for i in api.home_timeline(count=1000):
    result.append(i.text)
    print(i.text)

#print(result)
