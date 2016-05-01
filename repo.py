import sys,os
import urllib2
import json
from datetime import date 

class RepoTrend:
    def __init__(self, config_file):
        self.__set_script_path()
        self.config_file = self.path + "/" + config_file 
        self.__load_config()

    def __load_config(self):
        config = file(self.config_file)
        paras  = json.load(config)
        user   = paras["user"]
        repo   = paras["repo"]
        self.url = "https://api.github.com/repos/" + user + "/" + repo
        self.trend_file = self.path + "/" + paras["trend"] 

    def __set_script_path(self):
        path = sys.path[0]
        if os.path.isdir(path):
            self.path = path
        elif os.path.isfile(path):
            self.path = os.path.dirname(path)

    def getRemoteData(self):
        try:
            self.jsonData = urllib2.urlopen(self.url).read()
        except Exception,e:
            print e
            
    def saveJsonFile(self):
        file = open(self.trend_file, "w")
        jsonStr = json.dumps(self.trend)
        file.write(jsonStr)
        file.close()

    def parseJsonFile(self):
        trend = file(self.trend_file)
        self.trend = json.load(trend)

    def addTodayData(self):
        value = json.loads(self.jsonData)

        today = date.today().isoformat()
        fork  = value['forks_count']
        star  = value['stargazers_count']

        self.trend["date"].append(today);
        self.trend["fork"].append(fork);
        self.trend["star"].append(star);
        
if __name__ == "__main__":
    repoTrend = RepoTrend("./config.json")
    repoTrend.parseJsonFile()
    repoTrend.getRemoteData()
    repoTrend.addTodayData()
    repoTrend.saveJsonFile()
    
    
import sys,os
def cur_file_dir():
     path = sys.path[0]
     if os.path.isdir(path):
         return path
     elif os.path.isfile(path):
         return os.path.dirname(path)

print cur_file_dir()
