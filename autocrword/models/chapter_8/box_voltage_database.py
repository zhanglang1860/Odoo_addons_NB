import pandas as pd
import math

col_name = ['Turbinecapacity', 'convertingstation', 'long', 'width', 'high', 'Wallthickness', 'Highpressure',
            'C35concretetop', 'C15cushion', 'MU10brick', 'Reinforcement', 'area'
            ]

Data = pd.read_excel('风机基础数据.xlsx', header=1,sheet_name='箱变基础数据',usecols=col_name)

data = Data.loc[Data['Fortificationintensity'] == 7].loc[Data['Basictype'] == '扩展基础'].loc[Data['Ultimateload'] == 70000]


def excavation_cal(basic_earthwork_ratio, basic_stone_ratio):
    earth_excavation = math.pi * (data['FloorradiusR'] + 1.3) ** 2 * (
            data['H1'] + data['H2'] + data['H3'] + 0.15) * basic_earthwork_ratio
    stone_excavation = math.pi * (data['FloorradiusR'] + 1.3) ** 2 * (
            data['H1'] + data['H2'] + data['H3'] + 0.15) * basic_stone_ratio
    earthwork_backfill = earth_excavation + stone_excavation - data['Volume'] - data['Cushion']

    return earth_excavation, stone_excavation, earthwork_backfill


earth_excavation, stone_excavation, earthwork_backfill = excavation_cal(0.8, 0.2)
data['Earthexcavation'] = earth_excavation
data['Stoneexcavation'] = stone_excavation
data['Earthworkbackfill'] = earthwork_backfill
print(data['Earthexcavation'])





