import tweepy

consumer_key = 'XXXX'
consumer_secret = 'XXXX'

access_key = 'XXXX'
access_secret = 'XXXX'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth)
api.update_status('This is a message sent from Python')