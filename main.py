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

import excel2json

excel2json.convert_from_file('constants.xlsx')
