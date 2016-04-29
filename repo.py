import types
import urllib2
import json
from datetime import date 


def registerUrl():
    try:
        url ="https://api.github.com/repos/guodongxiaren/README"
        data = urllib2.urlopen(url).read()
        return data
    except Exception,e:
        print e
		
def saveJsonFile(fileName, fileData):
	file = open(fileName,"w")
	jsonStr = json.dumps(fileData)
	file.write(jsonStr)
	file.close()

def parseJsonFile(fileName):
	f = file(fileName)
	s = json.load(f)
	return s

def addTodayData(trend, jsonData):
	value = json.loads(jsonData)

	today = date.today().isoformat()
	fork  = value['forks_count']
	star  = value['stargazers_count']

	trend["date"].append(today);
	trend["fork"].append(fork);
	trend["star"].append(star);
	
if __name__ == "__main__":
	trend = parseJsonFile("trend.json")
	data = registerUrl()
	addTodayData(trend, data)
	saveJsonFile("trend.json", trend)
	
	
