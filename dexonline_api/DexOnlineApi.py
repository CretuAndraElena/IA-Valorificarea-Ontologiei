import json
import requests
from lxml import html
from unidecode import unidecode

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
    basicUrl = "https://dexonline.ro/definitie/"
    for word in words:
        dexDefinitions = []
        urlString = basicUrl + word + "?format=json"
        result = requests.get(urlString).json()
        ParseJson(result['definitions'], dexDefinitions)

        wordsDefinitions[word] = dexDefinitions

    return (json.dumps(wordsDefinitions, indent=2))


print(CreateApiLink(['biologie', 'animal']))