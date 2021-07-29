import json

with open('constants.json', 'r') as f:
    const = json.load(f)


def getValueFromConst(type, value):
    for i in const[type]:
        if i[type] == value:
            return i['value']


#print(getValueFromConst('CO2', 'Adiabatic exponent'))

with open('variables.json', 'r') as f:
    variant = json.load(f)


def getValueFromVariant(type, value):
    for i in variant[type]:
        if i[type] == value:
            return i['value']

print(getValueFromVariant('var', 'pressures'))