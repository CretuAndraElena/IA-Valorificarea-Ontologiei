import json


if __name__ == '__main__':
    with open('jsonfile.txt') as f:
        big_data = json.load(f)

    keys = {"_total_number_of_objects": len(big_data)}
    different_stuff = {}
    for obj_id in big_data:
        obj = big_data[obj_id]
        for key in obj:
            if key not in keys:
                keys[key] = {"nr_aparitii": 1}
            else:
                keys[key]["nr_aparitii"] += 1
            if isinstance(obj[key], dict):
                for key2 in obj[key]:
                    if key2 not in keys[key]:
                        keys[key][key2] = {"nr_aparitii": 1}
                    else:
                        keys[key][key2]["nr_aparitii"] += 1
                    if not (isinstance(obj[key][key2], basestring) or isinstance(obj[key][key2], list)):
                        different_stuff["%s_2" % key2] = obj
            elif not isinstance(obj[key], basestring):
                different_stuff["%s_1" % key] = obj

    with open("extracted_keys.txt", "wt") as f:
        f.write(json.dumps(keys, indent=4, sort_keys=True))
    with open("extracted_diff.txt", "wt") as f:
        f.write(json.dumps(different_stuff, indent=4, sort_keys=True))
