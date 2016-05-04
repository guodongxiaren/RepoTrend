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

    def get_remote_data(self):
        try:
            self.jsonData = urllib2.urlopen(self.url).read()
        except Exception,e:
            print e
            
    def save_json_file(self):
        file = open(self.trend_file, "w")
        jsonStr = json.dumps(self.trend)
        file.write(jsonStr)
        file.close()

    def parse_json_file(self):
        trend = file(self.trend_file)
        self.trend = json.load(trend)

    def add_today_data(self):
        value = json.loads(self.jsonData)

        today = date.today().isoformat()
        fork  = value['forks_count']
        star  = value['stargazers_count']

        self.trend["date"].append(today);
        self.trend["fork"].append(fork);
        self.trend["star"].append(star);
        
if __name__ == "__main__":
    repoTrend = RepoTrend("./config.local.json")
    repoTrend.parse_json_file()
    repoTrend.get_remote_data()
    repoTrend.add_today_data()
    repoTrend.save_json_file()
    
    
