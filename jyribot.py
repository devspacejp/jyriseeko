#Jyrinäbotin bottifilu

import tweepy
from rss_feedparser import *
from jyri_sala import *

auth = tweepy.OAuthHandler('Bir7wkC2C1xq20dLEjWqiAqNR','Bkfmo67REUIw9V9cCCXmlYW8NXYt6LQ3foF4YsdxnOaU2z8dA2')
auth.set_access_token('878179836430356480-P6DvYVPjUkCazIH1SIVBvMzAKeJCgu7','TOATtIOreRbvd2Hxym4NwAnNbXxBS8zMuIuCKwBCasSP3')
api = tweepy.API(auth)

#api.update_status(status='Tämä on testitwiitti, kohta jyrisee')
#api.create_friendship(id='436868527')
#api.update_status(status= item.title + item.link)			tähän käskyyn results listalta, lisää myöhemmin.