import component

c1CH4 = component.getValueFromConst('CH4', 'Molar mass')                              # Молярная масса метана
c2CH4 = component.getValueFromConst('CH4', 'Gas constant')                            # Газовая постоянна метана
c3CH4 = component.getValueFromConst('CH4', 'Adiabatic exponent')                      # Показатель адиабаты метана
c4CH4 = component.getValueFromConst('CH4', 'Absolute density')                        # Абсолютная плотность метана
c5CH4 = component.getValueFromConst('CH4', 'Relative density')                        # Относительная плотность метана
c6CH4 = component.getValueFromConst('CH4', 'Heat of combustion')                      # Теплота сгорания метана
c7CH4 = component.getValueFromConst('CH4', 'The amount of oxidizer for combustion')   # Объем окислителя для горения метана

c1CO2 = component.getValueFromConst('CO2', 'Molar mass')                              # Молярная масса диоксида
c2CO2 = component.getValueFromConst('CO2', 'Gas constant')                            # Газовая постоянна диоксида
c3CO2 = component.getValueFromConst('CO2', 'Adiabatic exponent')                      # Показатель адиабаты диоксида
c4CO2 = component.getValueFromConst('CO2', 'Absolute density')                        # Абсолютная плотность диоксида
c5CO2 = component.getValueFromConst('CO2', 'Relative density')                        # Относительная плотность диоксида
c6CO2 = component.getValueFromConst('CO2', 'Heat of combustion')                      # Теплота сгорания диоксида
c7CO2 = component.getValueFromConst('CO2', 'The amount of oxidizer for combustion')   # Объем окислителя для горения диоксида

c1air = component.getValueFromConst('air', 'Absolute density')                        # Абсолютная плотность воздуха


v1 = component.getValueFromVariant('var', 'Methane')                                          # процентное содержание метана
v2 = component.getValueFromVariant('var', 'Carbon dioxide')                                   # процентное содержание диоксида углерода
v3 = component.getValueFromVariant('var', 'pressures')                                        # давление газа
v4 = component.getValueFromVariant('var', 'N =')                                              # мощность газовой горелки
v5 = component.getValueFromVariant('var', 'alpha')                                            # значение коэф. первичного воздуха
v6 = component.getValueFromVariant('var', '(start) t =')                                      # начальная температура газа
v7 = component.getValueFromVariant('var', 'Atmosphere pressure')                              # атмосферное давление
v8 = component.getValueFromVariant('var', 'diameter')                                         # диаметр отверстия круглого сечения
v9 = component.getValueFromVariant('var', 'stepd')                                            # шаг для диаметра
v10 = component.getValueFromVariant('var', 'width')                                           # ширина отверстия прямоугольного сечения
v11 = component.getValueFromVariant('var', 'stepw')                                           # шаг ширины отверстия прямоугольного сечения
v12 = component.getValueFromVariant('var', 'height')                                          # высота отверстия прямоугольного сечения
v13 = component.getValueFromVariant('var', 'steph')                                           # шаг высоты отверстия прямоугольного сечения
v14 = component.getValueFromVariant('var', 'Fire holes')                                      # кол-во огневых отверстий газовой горелки
v15 = component.getValueFromVariant('var', 'Coef. Head bore flow rate')                       # коэф. расхода отверстий головки горелки
v16 = component.getValueFromVariant('var', 'Coef. Burner nozzle flow')                        # коэф. расхода сопла горелки
v17 = component.getValueFromVariant('var', 'Coef. Loss of ejection tube (1.5 or 2.1 or 3)')   # коэф. потерь эжекционной трубки
v18 = component.getValueFromVariant('var', 'Burner cover temperature')                        # температура крышки горелки
v19 = component.getValueFromVariant('var', 'Coef. Heat transfer int. P. cover')               # коэф. теплоотдачи внутренней пов-ти крышки