import json

with open('constants.json', 'r') as f:
    const = json.load(f)


def getValueFromConst(type, value):
    for i in const[type]:
        if i[type] == value:
            return i['value']


print(getValueFromConst('CH4', 'Gas constant'))
