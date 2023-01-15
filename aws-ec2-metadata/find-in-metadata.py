import requests
import json

def get_data():
    def createjson(get_metadata_url, metadata):
        output = {}
        for item in metadata:
            new_url = get_metadata_url + item
            i = requests.get(new_url)
            text = i.text         
            if item[-1] == "/":
                list_of_values = i.text.splitlines()
                output[item[:-1]] = createjson(new_url, list_of_values)
            elif check_json(text):
                output[item] = json.loads(text)
            else:
                output[item] = text
        return output

    def check_json(myjson):
        try:
            json.loads(myjson)
        except ValueError:
            return False
        return True


    get_metadata_url = 'http://169.254.169.254/latest/'
    metadata = ["meta-data/"]
    result = createjson(get_metadata_url, metadata)
    return result


def gen_dict_extract(key, var):
    if hasattr(var, 'items'):
        for k, v in var.items():
            if k == key:
                yield v
            if isinstance(v, dict):
                for result in gen_dict_extract(key, v):
                    yield result
            elif isinstance(v, list):
                for d in v:
                    for result in gen_dict_extract(key, d):
                        yield result


def find_key(key):
    metadata_output = get_data()
    return list(gen_dict_extract(key, metadata_output))

key = input("What key would you like to find?\n")
print(find_key(key))

