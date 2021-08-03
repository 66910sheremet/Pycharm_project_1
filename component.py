import json

with open('resources/constants.json', 'r') as f:
    const = json.load(f)

with open('resources/variables.json', 'r') as f:
    variant = json.load(f)


def getValueFromConst(type, name):
    for i in const[type]:
        if i[type] == name:
            return i['value']
        else:
            continue


def getValueFromVariant(type, name):
    for i in variant[type]:
        if i[type] == name:
            return i['value']
        else:
            continue
