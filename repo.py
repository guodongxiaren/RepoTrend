import types
import urllib2
import json
from datetime import date 

class RepoTrend:
    def __init__(self):
        self.url = "https://api.github.com/repos/guodongxiaren/README"
        # self.getRemoteData()

    def getRemoteData(self):
        try:
            self.jsonData = urllib2.urlopen(self.url).read()
        except Exception,e:
            print e
            
    def saveJsonFile(self, fileName):
        file = open(fileName,"w")
        jsonStr = json.dumps(self.trend)
        file.write(jsonStr)
        file.close()

    def parseJsonFile(self, fileName):
        f = file(fileName)
        self.trend = json.load(f)

    def addTodayData(self):
        value = json.loads(self.jsonData)

        today = date.today().isoformat()
        fork  = value['forks_count']
        star  = value['stargazers_count']

        self.trend["date"].append(today);
        self.trend["fork"].append(fork);
        self.trend["star"].append(star);
        
if __name__ == "__main__":
    repoTrend = RepoTrend()
    repoTrend.parseJsonFile("/home/jelly/github/repotrend/trend.json")
    repoTrend.getRemoteData()
    repoTrend.addTodayData()
    repoTrend.saveJsonFile("/home/jelly/github/repotrend/trend.json")
    
    
