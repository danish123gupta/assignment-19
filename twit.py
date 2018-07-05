from keys import consumer_key,consumer_secret,access_secret,access_token
import tweepy
oauth = tweepy.OAuthHandler(consumer_key,consumer_secret)
oauth.set_access_token(access_secret,access_token)
api = tweepy.API(oauth)
print(api.search("#sanju"))

user = api.get_user("vivek_shivam007")
print(user.screen_name)
print(user.followers_count)from keys import consumer_key,consumer_secret,access_secret,access_token
import tweepy
oauth = tweepy.OAuthHandler(consumer_key,consumer_secret)
oauth.set_access_token(access_secret,access_token)
api = tweepy.API(oauth)
print(api.search("#sanju")
#q.no.4
# Difference between a library and an API
#API is a part of library which defines how an application communicates with external code
#API can be written in any language.
#Library is written in same language which is a collection of all the functionalities required for the use case

