import openpyxl                                               # утановил пакет для парсинга excel
book = openpyxl.open('constants.xlsx', read_only=True)        # открыл файл с заготовкой сонстант
sheet = book.active                                           # открыл нужную страницу, ну как бы первую
consntants_CH4 = []                                             # создал пустой список
for row in range(2,9):                                        # создал цикл с перебором значений колонки [1]
    CH4_par = sheet[row][1].value                             # распарсил эту колонку
    consntants_CH4.append(CH4_par)                              # записал значения в список
print(consntants_CH4)                                           # вывел

# начало положено)