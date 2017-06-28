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
results_title = []
results_link = []

#for-loop sananetsintään listalta
while True:
	for feed in feeds:	#for-loop käy listaa läpi
		a = feedparser.parse(feed)
		for item in a.entries:			#for-loop etsii listalta löytyvän linkin syötteestä sanaa
			if 'jyräh' in item.title:	#jos otsikossa etsittävä sana, tulostaa otsikon ja linkin
				print(item.title)		#printit testailuu
				print(item.link,'\n')
				results_title.append(item.title) #pitääkö title ja linkki tallentaa eri listoihin?
				results_link.append(item.link)
				print(results_title,'\n')
				print(results_link,'\n')	
			elif 'jyris' in item.title:
				print(item.title)
				print(item.link)
				print('\n')
				results_title.append(item.title)
				results_link.append(item.link)			
				print(results_title,'\n')
				print(results_link,'\n')	
				break
	time.sleep(30)	

	