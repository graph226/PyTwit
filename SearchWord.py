import twpy
api = twpy.api
query = "料理"

# search limit is maybe 200
for tweet in api.Cursor(q=query,count=200):
    print(tweet.created_at, tweet.user.screen_name, tweet.text)
