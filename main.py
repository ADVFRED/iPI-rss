import configparser
from xml.dom import minidom
import requests_xml
import os
import glob
#declarations
PodcastsNames = []
PodcastsRSS = []
PodcastCombo = []  #format pc: [('podcast1',podcast1.xml)]

#cfg setup
config = configparser.ConfigParser()
config.read("config.cfg")


if config["SETUP"]["ResetCfg"] == "True":
	abspath = os.path.abspath(__file__)
	dname = os.path.dirname(abspath)
	os.chdir(dname)
	os.mkdir("xml_cache")
	config["SETUP"]["ResetCfg"]=False

#cfg parsing
for name in config["RSS Feeds"]["PodcastNames"].strip("[]").split(","):
    #print(f"{name}")
    PodcastsNames.append(name)
for url in config["RSS Feeds"]["PodcastURL"].strip("[]").split(","):
    #print(f"{url}")
    PodcastsRSS.append(url)
assert len(PodcastsNames) == len(PodcastsRSS)
for x in range(len(PodcastsNames)):
	PodcastCombo.append((PodcastsNames[x],PodcastsRSS[x]))
print(f"{PodcastCombo}")

#Directory setup/verifiction
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
os.chdir("xml_cache")
print(str(os.getcwd()))
podcastDirectories=[ p.replace('/', '') for p in glob.glob('*/') ]
print(str(podcastDirectories))

for pdcstname in PodcastsNames:
	dirs=os.walk(os.getcwd())
	if pdcstname in podcastDirectories:
		pass
	else:
		os.mkdir(pdcstname)
		os.chdir(pdcstname)
		
#Grab XML files and store to xml_cache
for podcast in PodcastCombo:
	abspath = os.path.abspath(__file__)
	dname = os.path.dirname(abspath)
	os.chdir(dname+'/xml_cache')
	#print('start')
	#os.chdir("/home/runner/iPI-rss/xml_cache")
	#print(os.getcwd())
	#print(podcastDirectories)
	os.chdir(podcast[0])
	#print(os.getcwd())
	#This just in, I'm an actual idiot. ProTip: Make sure your print statements are *after* the code your debugging
	#^^^

	#req=requests.get(podcast[1], allow_redirects=True)
	#open(podcast[0]+'.xml', 'wb').write(req.content)

#RSS feed parsing
#RssXml=minidom.parse(PodcastCombo[0][1])