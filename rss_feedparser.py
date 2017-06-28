#Tämä on feedparser koodi Jyrinäbotille.

#Aikaviiveelle ja parserille kirjastot
import time
import feedparser
#lista läpikäytävistä syötteistä
feeds=['http://www.iltalehti.fi/rss.xml', 'http://www.is.fi/rss/tuoreimmat.xml',
'https://www.mtv.fi/api/feed/rss/uutiset_uusimmat','http://www.kaleva.fi/rss/show/',
'https://www.aamulehti.fi/?feed=uutiset&o=Tuoreimmat&k=0&ma=0&c=9,6,2,8,4,11,7,3,10,5'
]

#Taulukko löydetyille tuloksille
results = []

#for-loop sananetsintään listalta
while True:
	for feed in feeds:	#for-loop käy listaa läpi
		a = feedparser.parse(feed)
		for item in a.entries:			#for-loop etsii listalta löytyvän linkin syötteestä sanaa
			if 'nainen' in item.title:	#jos otsikossa etsittävä sana, tulostaa otsikon ja linkin
				print(item.title)
				print(item.link)
				print('\n')
				results.append(item) #pitääkö title ja linkki tallentaa eri listoihin?
			elif 'jyris' in item.title:
				print(item.title)
				print(item.link)
				print('\n')
				results.append(item) #pitääkö title ja linkki tallentaa eri listoihin?
	time.sleep(30)	