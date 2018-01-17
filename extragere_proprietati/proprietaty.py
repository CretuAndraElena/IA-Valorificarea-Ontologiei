import re
import json

json_file = open("inputJson.json", "r")

json_words = json.loads(json_file.read())
definitions = open("finalJson_prop.json", "w")


def extract_proprety():
    num = {}
    arry =[]
    definitions.write('{ \n')
    for object in json_words:
        definitions.write( '\"'+json_words[object]['name'] +'\" :'+'{ \n'+ '\"id\"'+ ' : \"'+ json_words[object]['id']+'\"' + ',  \n')

        definitions.write('\"nume\"'+ ' : \"'+'is_a' +'\"' + ',  \n')
        aux =str(json_words[object]['relations']['is_a'][0])
        if aux in json_words :
            definitions.write(
                '\"parinte\"' + ' : \"' + json_words[aux]['id'] + '\"' + ' \n' + ' } ,\n')
        else :
            definitions.write('\"parinte\"' + ' : ' + 'null' + ' \n' + ' } ,\n')

    definitions.write('} \n')

extract_proprety()
json_file.close()
definitions.close()