import configparser
from xml.dom import minidom
import os

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

for pdcstname in PodcastsNames:
	dirs=dir()
	if pdcstname in dirs:
		pass
	else:
		os.mkdir(pdcstname)
		os.chdir(pdcstname)
		


#RSS feed parsing
#RssXml=minidom.parse(PodcastCombo[0][1])