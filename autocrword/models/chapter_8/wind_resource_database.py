import pandas as pd
import math
from docxtpl import DocxTemplate
import numpy as np
from RoundUp import round_up

col_name = ['Fortificationintensity', 'Bearingcapacity', 'Basictype', 'Ultimateload', 'FloorradiusR', 'R1', 'R2', 'H1',
            'H2', 'H3', 'Pilediameter', 'number', 'length', 'Singlepilelength', 'Area', 'Volume', 'Cushion',
            'M48PrestressedAnchor', 'C80secondarygrouting']

Data = pd.read_excel('风机基础数据.xlsx', header=1, sheet_name='风机基础数据', usecols=col_name)

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
data['Reinforcement'] = data['Volume'] * 0.1
data_np = np.array(data)
print(data_np[0])

# Dict = {'土方开挖': data['Earthexcavation'],2),
#         '石方开挖': data['Stoneexcavation'],2),
#         '土石方回填': data['Earthworkbackfill'],2),
#         'C40混凝土': data['Volume'],2),
#         'C15混凝土': data['Cushion'],2),
#         '钢筋': data['Volume'] * 0.1,
#         '基础防水': 1,
#         '沉降观测': 4,
#         '预制桩长': data['Singlepilelength'],2),
#         'M48预应力锚栓': data['M48PrestressedAnchor'],2),
#         'C80二次灌浆': data['C80secondarygrouting']
#         }

Dict = {
    '土方开挖': round_up(data_np[0, 19], 2),
    '石方开挖': round_up(data_np[0, 20], 2),
    '土石方回填': round_up(data_np[0, 21], 2),
    'C40混凝土': round_up(data_np[0, 15], 2),
    'C15混凝土': round_up(data_np[0, 16], 2),
    '钢筋': round_up(data_np[0, 22], 2),
    '基础防水': 1,
    '沉降观测': 4,
    '预制桩长': round_up(data_np[0, 13], 2),
    'M48预应力锚栓': round_up(data_np[0, 17], 2),
    'C80二次灌浆': round_up(data_np[0, 18])
}

# print(Dict)

tpl = DocxTemplate(r'C:\Users\Administrator\PycharmProjects\wind_model\CR_chapter8_template.docx')
tpl.render(Dict)
# print(Dict)
tpl.save(r'C:\Users\Administrator\PycharmProjects\wind_model\result_chapter8_a.docx')
