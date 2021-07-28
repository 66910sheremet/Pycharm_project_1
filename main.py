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
with open('constants.json','r') as file:
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

with open('constants.json','r') as file:
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