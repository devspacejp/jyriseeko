#Jyrinäbotin bottifilu

import tweepy
#from rss_feedparser import *
from jyri_sala import *

auth = tweepy.OAuthHandler('your_consumer_key','your_consumer_secret')
auth.set_access_token('your_access_token','your_access_secret')
api = tweepy.API(auth)

#api.update_status(status='Uusi testi')
#api.create_friendship(id='436868527')
#api.update_status(status= item.title + item.link)			tähän käskyyn results listalta, lisää myöhemmin.