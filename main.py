# import openpyxl                                               # утановил пакет для парсинга excel
# book = openpyxl.open('constants.xlsx', read_only=True)        # открыл файл с заготовкой сонстант
# sheet = book.active                                           # открыл нужную страницу, ну как бы первую
# consntants_CH4 = []                                             # создал пустой список
# for row in range(2,9):                                        # создал цикл с перебором значений колонки [1]
#    CH4_par = sheet[row][1].value                             # распарсил эту колонку
#    consntants_CH4.append(CH4_par)                              # записал значения в список

# import pandas

# excel_data_df = pandas.read_excel('constants.xlsx',
# sheet_name='const')
# json_str = excel_data_df.to_json()
# json_str = excel_data_df.to_json(orient='records')
# print('Excel Sheet to JSON:\n', json_str)

# import json
# with open('constants.json', 'r', encoding='utf-8', errors='ignore') as f:
#   text = json.load(f)
#   print(text)

import json

with open('constants.json', 'r') as file:
    constanty = json.load(file)
# print(constanty['CH4'])
b = []
for CH4 in constanty['CH4']:
    b.append(CH4['value'])
CH4c1 = b[0]
CH4c2 = b[1]
CH4c3 = b[2]
CH4c4 = b[3]
CH4c5 = b[4]
CH4c6 = b[5]
CH4c7 = b[6]
# print(CH4c1, CH4c2, CH4c3, CH4c4, CH4c5, CH4c6, CH4c7)

with open('constants.json', 'r') as file:
    constanty = json.load(file)
# print(constanty['CO2'])
c = []
for CO2 in constanty['CO2']:
    c.append(CO2['value'])
CO2c1 = c[0]
CO2c2 = c[1]
CO2c3 = c[2]
CO2c4 = c[3]
CO2c5 = c[4]
CO2c6 = c[5]
CO2c7 = c[6]
# print(CO2c1, CO2c2, CO2c3, CO2c4, CO2c5, CO2c6, CO2c7)

with open('constants.json', 'r') as file:
    constanty = json.load(file)
# print(constanty['CO2'])
d = []
for air in constanty['air']:
    d.append(air['value'])
airc1 = d[0]


# print(airc1)

class Constant:
    CH4c1 = b[0]
    CH4c2 = b[1]
    CH4c3 = b[2]
    CH4c4 = b[3]
    CH4c5 = b[4]
    CH4c6 = b[5]
    CH4c7 = b[6]
    CO2c1 = c[0]
    CO2c2 = c[1]
    CO2c3 = c[2]
    CO2c4 = c[3]
    CO2c5 = c[4]
    CO2c6 = c[5]
    CO2c7 = c[6]
    airc1 = d[0]


with open('variables.json', 'r') as file:
    variables = json.load(file)
per = []
for var in variables['var']:
    per.append(var['value'])
per1 = per[0]
per2 = per[1]
per3 = per[2]
per4 = per[3]
per5 = per[4]
per6 = per[5]
per7 = per[6]
per8 = per[7]
per9 = per[8]
per10 = per[9]
per11 = per[10]
per12 = per[11]
per13 = per[12]
per14 = per[13]
per15 = per[14]
per16 = per[15]
per17 = per[16]
per18 = per[17]
per19 = per[18]


# print(per1,per2,per3,per4,per5,per6,per7,per8,per9,per10,per11,per12,per13,per14,per15,per16,per17, per18, per19)

class Variables:
    per1 = per[0]
    per2 = per[1]
    per3 = per[2]
    per4 = per[3]
    per5 = per[4]
    per6 = per[5]
    per7 = per[6]
    per8 = per[7]
    per9 = per[8]
    per10 = per[9]
    per11 = per[10]
    per12 = per[11]
    per13 = per[12]
    per14 = per[13]
    per15 = per[14]
    per16 = per[15]
    per17 = per[16]
    per18 = per[17]
    per19 = per[18]
