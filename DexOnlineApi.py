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

    return wordsDefinitions


def IntegrateInBigJson(file_name):
    with open(file_name, 'rt') as f:
        ontology_dict = json.loads(f.read())
    concepts = ontology_dict.keys()
    for concept in concepts:
        ontology_dict[concept]["Definitii"] = CreateApiLink([concept])[concept]
    # print(json.dumps(ontology_dict, indent=4))
    with open('json_ontologie_definitii_sinonime_paronime.json', 'wt') as f:
        f.write(json.dumps(ontology_dict, indent=4))


IntegrateInBigJson("paronime.json")
