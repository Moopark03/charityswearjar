import tweepy


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
for tweet in tweepy.Cursor(api.search, q=('fuck OR shit OR motherfucker OR cunt OR shithead OR fucking -filter:retweets -filter:replies'), lang='en', page=2).items(numberOfTweets):
    tweet.retweet()

#Things to work on:
### 1. Scan tweets older than 1 hour