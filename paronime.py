import json
import requests
import re

def getParonyms (words):
    paronyms = dict()
    pWords = []
    basicUrl = "http://dex.dictoo.eu/index.php?cheie="
    endUrl = "&m=6"
    words = list(map(lambda x:re.sub(":", " ", x), words))

    for word in words:
        requestUrl = basicUrl + word + endUrl
        result = requests.get(requestUrl).text.split(" ")
        for element in result:
            if(matchesToPattern(element)):
                pWords.append(element)
        paronyms[word] = formatWords(pWords)
        pWords.clear()

    return paronyms

def matchesToPattern(word):
    pattern = re.compile("(.)*index\.php\?cheie=(.)*")
    return pattern.match(word)

def formatWords(words):
    keyword = "cheie="
    formatedWords = []
    for word in words:
        word = word[word.find(keyword):word.find("\"", word.find(keyword)+keyword.__len__())]
        word = re.sub(keyword, '', word)
        if(word.find("%") < 0):
            formatedWords.append(word)

    return formatedWords

def loadDataToJsonFile(jsonFileName, jsonData, paronyms):

    for key, value in paronyms.items():
        key = re.sub(" ", ":", key)
        jsonData[key]["Paronime"] = value

    open(jsonFileName, "w").write(json.dumps(jsonData, indent=2))

jsonElements = []
jsonFileName = "paronime.json"

with open(jsonFileName) as jsonFile:
    data = json.load(jsonFile)

jsonElements=list(data)
paronyms = getParonyms(jsonElements)

loadDataToJsonFile(jsonFileName, data, paronyms)
