import json
import requests
from lxml import html
from unidecode import unidecode
import re
import itertools
from pprint import pprint

def ParseJson(definitions, dexDefinitions):
    for definition in definitions:
        defHtmlRep = definition['htmlRep']

        htmlFragments = html.fragments_fromstring(defHtmlRep)
        root = html.Element('root')
        for fragment in htmlFragments:
            root.append(fragment)

        result = unidecode(root.text_content())
        dexDefinitions.append(result)


def CreateApiLink(words):
    wordsDefinitions = {}
    basicUrl = "https://dexonline.ro/definitie-sinonime/"
    for word in words:
        dexDefinitions = []
        urlString = basicUrl + word + "?format=json"
        result = requests.get(urlString).json()
        ParseJson(result['definitions'], dexDefinitions)
        wordsDefinitions[word] = dexDefinitions
    jsonKey,jsonSinonims=ExtractSinonims(wordsDefinitions)
    with open('jsonfile.json') as json_file:  
    	data = json.load(json_file)
	for key in jsonKey:
		data[key]["Sinomime"]=jsonSinonims[key]

    return json.dumps(data, indent=2)
def ExtractSinonims(sinonims):
	listOfSinonims=dict()
	for (key,value) in sinonims.items():
		newvalue=re.split("[0-9].",str(value))
		newvalue=map(lambda x:re.sub("(\(.*\))|(adv\.)|(adj\.)|(v\.)|(s\.)|('])|\.|;",'',x),newvalue)
		newvalue=map(lambda x:x.split(","),newvalue)
		newvalue=list(itertools.chain.from_iterable(newvalue[1:]))
		listOfSinonims[key]=filter(lambda x:x is not "",newvalue)	
	return (list(listOfSinonims),listOfSinonims)
#fisierSinonime=open("FisiereSinonime","w").write(CreateApiLink(['creier','epifiza', 'sange']))

a=[]
with open('jsonfile.json') as json_file:  
    data = json.load(json_file)
a=list(data)
fisierSinonime=open("FisiereSinonime.json","w").write(CreateApiLink(a))




