import json

MaxCMD =11


def json_show_all_commands():
#Local paths start from the root of the project
    with open('jsonfiles/files/sample.json', 'r') as json_file:
        data = json.load(json_file)

    for i in range(0,MaxCMD):
        print(data[i]["cmd"])

def json_parsing():

    with open('jsonfiles/files/sample.json', 'r') as json_file:
        data = json.load(json_file)

    for i in range(0,MaxCMD):
        print(data[i]["cmd"])

#url = urllib2.urlopen('https://github.com/....')
#obj = json.load(url)

