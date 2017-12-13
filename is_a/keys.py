import re
import json

json_file = open("jsonfile.txt", "r")

json_words = json.loads(json_file.read())
definitions = open("output_def.txt", "w")


def extract_proprety():
    num = 0
    for object in json_words:
        print(json_words[object]["name"])
        definitions.write(json_words[object]["name"]+' : \n')
        if "relations" in json_words[object]:
            for relations in json_words[object]["relations"]:
                if ("is_a" == relations):
                  for is_a in json_words[object]["relations"]["is_a"]:
                      print('is_a ==> ',json_words[is_a]["name"])
                      definitions.write('is_a ==> ' + json_words[is_a]["relations"] + '  \n')
                if ("can_be" == relations):
                  for can_be in json_words[object]["relations"]["can_be"]:
                      print('can_be ==> ',json_words[can_be]["name"])
                      definitions.write('can_be ==> '+ json_words[can_be]["name"] + '  \n')
        else:
            definitions.write('no definitions find')

        definitions.write('\n \n')
        num = num + 1


extract_proprety()
json_file.close()
definitions.close()
