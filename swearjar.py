import tweepy

consumer_key = '6YOHP51iK3EwFTH1gBKlM8L2q'
consumer_secret = 'ObafnJUoLwnRR8TxSMyN0SrF5q3AnomHDNvtjx3BTDAb0Ta45a'
access_token = '1140328953929801728-IDWvSF2PE0qWjqTXfEdDWsjijef2bp'
access_token_secret = 'au7LzwTX5k5x4PWv3z2Z6WKdgLqWD4qZaeb9uRUgRmubz'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
user = api.me()

for follower in tweepy.Cursor(api.followers).items():
    follower.follow()
    print("Followed everyone that is following " + user.name)

#load cuss words in txt
#f = open('swear.txt', 'r')
#search = f.read().splitlines()
#f.close()
#words contain all the keywords to search for

phrase = 'Bad words are not as bad as being selfish. Donate to a charity of the week: https://www.plannedparenthood.org/get-involved/other-ways-give'
numberOfTweets = 1
for tweet in tweepy.Cursor(api.search, q=('fuck OR shit OR motherfucker OR cunt OR shithead OR fucking -filter:retweets'), lang='en', page=2).items(numberOfTweets):
    tweet.retweet()

#Things to work on:
### 1. Scan tweets older than 1 hour