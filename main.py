import configparser
import feedparser

"""declarations"""
PodcastsNames = []
PodcastsRSS = []
PodcastCombo = []  #format pc: [('podcast1',podcast1.xml)]

"""cfg setup"""
config = configparser.ConfigParser()
config.read("config.cfg")

if config["SETUP"]["ResetCfg"] == True:
    pass  #reset cfg

"""cfg parsing"""
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

"""RSS feed parsing"""
