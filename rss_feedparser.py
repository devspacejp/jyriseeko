#Tämä on feedparser koodi Jyrinäbotille.

#Aikaviiveelle ja parserille kirjastot
import time
import feedparser
#lista läpikäytävistä syötteistä
feeds=['http://www.iltalehti.fi/rss.xml', 'http://www.is.fi/rss/tuoreimmat.xml',
'https://www.mtv.fi/api/feed/rss/uutiset_uusimmat','http://www.kaleva.fi/rss/show/',
'https://www.aamulehti.fi/?feed=uutiset&o=Tuoreimmat&k=0&ma=0&c=9,6,2,8,4,11,7,3,10,5',
'https://feeds.yle.fi/uutiset/v1/recent.rss?publisherIds=YLE_UUTISET',
'https://www.verkkouutiset.fi/feeds/all/rss'
]
#Kaikki title osiot poistettavissa, ei tarpeellisia. Ellei tee nimenetsintä featuree
#Listat löydetyille tuloksille
results_title1 = []
results_link1 = []
results_title2 = []
results_link2 = []
print(time.ctime())
#loopit sananetsintään listalta
def iParse():
	for feed in feeds:	#for-loop käy listaa läpi
		a = feedparser.parse(feed)
		for item in a.entries:			#for-loop etsii listalta löytyvän linkin syötteestä sanaa
			if 'jyräh' in item.title:		#jos otsikossa etsittävä sana, tulostaa otsikon ja linkin
				#item.title = (item.title[:110]) if len(item.title) > 110 else item.title	#jos otsikko liian pitkä lyhentää sen 110 characteriin, toimii
				results_title1.append(item.title)			
				results_link1.append(item.link)
				print(results_title1, '\n')
			elif 'jyris' in item.title:
				#item.title = (item.title[:110]) if len(item.title) > 110 else item.title #toimii
				results_title2.append(item.title)
				results_link2.append(item.link)			
				print(results_title2, '\n')
	else:
		print('feeds käyty läpi, 30min next', '\n')
	
	
