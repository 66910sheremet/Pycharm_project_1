import json

with open('constants.json', 'r') as f:
    const = json.load(f)


def getValueFromConst(type, value):
    for i in const[type]:
        if i[type] == value:
            return i['value']


c1CH4 = getValueFromConst('CH4', 'Molar mass') # Молярная масса метана
c2CH4 = getValueFromConst('CH4', 'Gas constant') # Газовая постоянна метана
c3CH4 = getValueFromConst('CH4', 'Adiabatic exponent') # Показатель адиабаты метана
c4CH4 = getValueFromConst('CH4', 'Absolute density') # Абсолютная плотность метана
c5CH4 = getValueFromConst('CH4', 'Relative density') # Относительная плотность метана
c6CH4 = getValueFromConst('CH4', 'Heat of combustion') # Теплота сгорания метана
c7CH4 = getValueFromConst('CH4', 'The amount of oxidizer for combustion') # Объем окислителя для горения метана

c1CO2 = getValueFromConst('CO2', 'Molar mass') # Молярная масса диоксида
c2CO2 = getValueFromConst('CO2', 'Gas constant') # Газовая постоянна диоксида
c3CO2 = getValueFromConst('CO2', 'Adiabatic exponent') # Показатель адиабаты диоксида
c4CO2 = getValueFromConst('CO2', 'Absolute density') # Абсолютная плотность диоксида
c5CO2 = getValueFromConst('CO2', 'Relative density') # Относительная плотность диоксида
c6CO2 = getValueFromConst('CO2', 'Heat of combustion') # Теплота сгорания диоксида
c7CO2 = getValueFromConst('CO2', 'The amount of oxidizer for combustion') # Объем окислителя для горения диоксида

c1air = getValueFromConst('air', 'Absolute density') # Абсолютная плотность воздуха

#print(c1CH4)

with open('variables.json', 'r') as f:
    variant = json.load(f)


def getValueFromVariant(type, value):
    for i in variant[type]:
        if i[type] == value:
            return i['value']

v1 = getValueFromVariant('var', 'Methane')         # процентное содержание метана
v2 = getValueFromVariant('var', 'Carbon dioxide')  # процентное содержание диоксида углерода
v3 = getValueFromVariant('var', 'pressures')       # давление газа
v4 = getValueFromVariant('var', 'N =')             # мощность газовой горелки
v5 = getValueFromVariant('var', 'alpha')           # значение коэф. первичного воздуха
v6 = getValueFromVariant('var', '(start) t =:')    # начальная температура газа
v7 = getValueFromVariant('var', 'Atmosphere pressure:')    # атмосферное давление
v8 = getValueFromVariant('var', 'diameter')         # диаметр отверстия круглого сечения
v9 = getValueFromVariant('var', 'stepd')            # шаг для диаметра
v10 = getValueFromVariant('var', 'width')         # ширина отверстия прямоугольного сечения
v11 = getValueFromVariant('var', 'stepw')         # шаг ширины отверстия прямоугольного сечения
v12 = getValueFromVariant('var', 'height')         # высота отверстия прямоугольного сечения
v13 = getValueFromVariant('var', 'steph')         # шаг высоты отверстия прямоугольного сечения
v14 = getValueFromVariant('var', 'Fire holes:')    # кол-во огневых отверстий газовой горелки
v15 = getValueFromVariant('var', 'Coef. Head bore flow rate:')    # коэф. расхода отверстий головки горелки
v15 = getValueFromVariant('var', 'Coef. Burner nozzle flow:')    # коэф. расхода сопла горелки
v16 = getValueFromVariant('var', 'Coef. Loss of ejection tube (1.5 or 2.1 or 3)')    # коэф. потерь эжекционной трубки
v17 = getValueFromVariant('var', 'Burner cover temperature')    # температура крышки горелки
v18 = getValueFromVariant('var', 'Coef. Heat transfer int. P. cover')    # коэф. теплоотдачи внутренней пов-ти крышки




print(v18)