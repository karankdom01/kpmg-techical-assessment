import requests
import json

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
metadata_json = json.dumps(result, indent=4, sort_keys=True)
print(metadata_json)
