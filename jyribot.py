#Jyrinäbotin bottifilu
import tweepy
import time
from rss_feedparser import *
from jyri_sala import *

auth = tweepy.OAuthHandler('Bir7wkC2C1xq20dLEjWqiAqNR','Bkfmo67REUIw9V9cCCXmlYW8NXYt6LQ3foF4YsdxnOaU2z8dA2')
auth.set_access_token('878179836430356480-P6DvYVPjUkCazIH1SIVBvMzAKeJCgu7','TOATtIOreRbvd2Hxym4NwAnNbXxBS8zMuIuCKwBCasSP3')
api = tweepy.API(auth)

print('miksi ei tule?')

tweet1 =''.join(results_link1) + ' #taas' ' #jyrahtaa'				#.join(results_title1)
tweet2 =''.join(results_link2) + ' #taas' ' #jyrisee'				#.join(results_title2)



if len(tweet1) > 23:
	api.update_status(status = tweet1)
	print(results_link1)
	#print(time.ctime())
	results_title1[:] = []
	results_link1[:] = []			#tyhjentää listan status updaten jälkeen
if len(tweet2) > 23:
	api.update_status(status = tweet2)
	print(results_link2)
	#print(time.ctime())
	results_title2[:] = []
	results_link2[:] = []			#tyhjentää listan status updaten jälkeen

