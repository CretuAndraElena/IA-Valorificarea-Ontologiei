import json

data = open("jsonfile.txt", "rt").read()
d = json.load(open("jsonfile.txt", "rt"))
index = 0
keys = ["desc", "id", "name", "hasExactSynonym", "namespace", "disjointWith", "hasAlternativeId", "subset", "xref", "is_a", "can_be"]
subdomenii = ['disjointWith', 'hasAlternativeId', 'hasExactSynonym', 'subset', 'xref', 'is_a', 'can_be', 'namespace']
apnumber = []
for k in keys:
    aparitii = 0
    for i in d.values():
        for j in i:
           if k==j:
                aparitii = aparitii + 1
           if (j=='other' or j=='relations') and (k in subdomenii):
            for x in i.values():
                for y in x:
                    if k==y:
                        aparitii = aparitii + 1
    apnumber += [aparitii]

for i in range(11):
    print (keys[i], apnumber[i])