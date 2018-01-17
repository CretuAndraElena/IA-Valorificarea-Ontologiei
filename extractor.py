import pronto

ontology = pronto.Ontology('1.owl', parser="OwlXMLParser")

jsonFile = open("jsonFile", "w")

jsonFile.write(ontology.json)
