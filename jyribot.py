#Jyrinäbotin bottifilu
import tweepy
import time
import urllib
import requests
from rss_feedparser import *
from jyri_sala import *

#Tähän authi tiedot, oikeat avaimet otettu pois.
auth = tweepy.OAuthHandler('consumer_key', 'consumer_secret')
auth.set_access_token('access_token','access_secret')
api = tweepy.API(auth)


link = "http://www.google.com"

def net_check(link):
	try:
		urllib.request.urlopen(link, timeout=1)
		return True
	except urllib.request.URLError:
		return False
	

while True:	
	net_check(link)
	print('Net check:',net_check(link))
	iParse()
	tweet1 =''.join(results_link1) + ' #taas' ' #jyrähti'				#.join(results_title1)
	tweet2 =''.join(results_link2) + ' #taas' ' #jyrisi'				#.join(results_title2)
	if "ummola" in results_title1 or results_title2:
		api.update_status(status = "Kalervooooooooo!!!")
	if len(tweet1) > 23:
		try:
			api.update_status(status = tweet1)
			print(time.ctime())
			print(results_title1)
			print(results_link1)
		except:
			tweepy.error.TweepError
		results_title1[:] = []
		results_link1[:] = []			#tyhjentää listan status updaten jälkeen
		time.sleep(2)
	if len(tweet2) > 23:
		try:
			api.update_status(status = tweet2)
			print(time.ctime())
			print(results_title2)
			print(results_link2)
		except:
			tweepy.error.TweepError
		results_title2[:] = []
		results_link2[:] = []			#tyhjentää listan status updaten jälkeen
		time.sleep(2)
	time.sleep(1800)
	
