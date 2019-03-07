import pandas as pd
import math, os
from docxtpl import DocxTemplate
import numpy as np
from RoundUp import round_up


class WindResourceDatabase:

    def __init__(self):
        self.Fortificationintensity, self.Ultimateload = 0, 0
        self.Basictype = ''
        self.basic_earthwork_ratio, self.basic_stone_ratio = 0, 0
        self.data = pd.DataFrame()
        self.data_timesnumber = pd.DataFrame()
        self.numbers = 0
        self.data_timesnumber_np, self.data_np, self.data_number_concat_np = [], [], []

    def extraction_data(self, Fortificationintensity, Basictype, Ultimateload):
        self.Fortificationintensity = Fortificationintensity
        self.Basictype = Basictype
        self.Ultimateload = Ultimateload
        col_name = ['Fortificationintensity', 'Bearingcapacity', 'Basictype', 'Ultimateload', 'FloorradiusR', 'R1',
                    'R2', 'H1', 'H2', 'H3', 'Pilediameter', 'number', 'length', 'Singlepilelength', 'Area', 'Volume',
                    'Cushion', 'M48PrestressedAnchor', 'C80secondarygrouting']

        Data = pd.read_excel(
            r'C:\Users\Administrator\PycharmProjects\Odoo_addons_NB\autocrword\models\chapter_8\chapter8database.xlsx',
            header=1, sheet_name='风机基础数据', usecols=col_name)
        self.data = Data.loc[Data['Fortificationintensity'] == self.Fortificationintensity].loc[
            Data['Basictype'] == self.Basictype].loc[Data['Ultimateload'] == 70000]
        return self.data

    def excavation_cal(self, basic_earthwork_ratio, basic_stone_ratio):
        self.basic_earthwork_ratio = basic_earthwork_ratio
        self.basic_stone_ratio = basic_stone_ratio
        self.earth_excavation = math.pi * (self.data['FloorradiusR'] + 1.3) ** 2 * (
                self.data['H1'] + self.data['H2'] + self.data['H3'] + 0.15) * self.basic_earthwork_ratio
        self.stone_excavation = math.pi * (self.data['FloorradiusR'] + 1.3) ** 2 * (
                self.data['H1'] + self.data['H2'] + self.data['H3'] + 0.15) * self.basic_stone_ratio
        self.earthwork_backfill = self.earth_excavation + self.stone_excavation - self.data['Volume'] - self.data[
            'Cushion']

        self.data['Earthexcavation'] = self.earth_excavation
        self.data['Stoneexcavation'] = self.stone_excavation
        self.data['Earthworkbackfill'] = self.earthwork_backfill
        self.data['Reinforcement'] = self.data['Volume'] * 0.1
        return self.data

    def data_numbers_cal(self, num):
        self.numbers = num
        for i in range(0, self.data.shape[1]):
            if self.data.iloc[:, i].dtype != 'object':
                self.data_timesnumber.at[0, i] = self.data.iloc[0, i] * self.numbers
            else:
                self.data_timesnumber.at[0, i] = self.data.iloc[0, i]
        self.data_timesnumber_np = np.array(self.data_timesnumber)
        self.data_np = np.array(self.data)
        self.data_number_concat_np = np.vstack([self.data_np, self.data_timesnumber_np])
        return self.data_number_concat_np


project01 = WindResourceDatabase()
data = project01.extraction_data(Basictype='扩展基础', Ultimateload=70000, Fortificationintensity=7)
numbers = 20
data_cal = project01.excavation_cal(0.8, 0.2)
data_number_concat = project01.data_numbers_cal(20)
print(data_number_concat)
Dict = {'numbers': numbers,
        '土方开挖_风机': round_up(data_number_concat[0, 19], 2), '土方开挖_风机numbers': round_up(data_number_concat[1, 19], 2),
        '石方开挖_风机': round_up(data_number_concat[0, 20], 2), '石方开挖_风机numbers': round_up(data_number_concat[1, 20], 2),
        '土石方回填_风机': round_up(data_number_concat[0, 21], 2), '土石方回填_风机numbers': round_up(data_number_concat[1, 21], 2),
        'C40混凝土_风机': round_up(data_number_concat[0, 15], 2), 'C40混凝土_风机numbers': round_up(data_number_concat[1, 15], 2),
        'C15混凝土_风机': round_up(data_number_concat[0, 16], 2), 'C15混凝土_风机numbers': round_up(data_number_concat[1, 16], 2),
        '钢筋_风机': round_up(data_number_concat[0, 22], 2), '钢筋_风机numbers': round_up(data_number_concat[1, 22], 2),
        '基础防水_风机': 1, '基础防水_风机numbers': 1 * numbers,
        '沉降观测_风机': 4, '沉降观测_风机numbers': 4 * numbers,
        '预制桩长_风机': round_up(data_number_concat[0, 13], 2), '预制桩长_风机numbers': round_up(data_number_concat[1, 13], 2),
        'M48预应力锚栓_风机': round_up(data_number_concat[0, 17], 2), 'M48预应力锚栓_风机numbers': round_up(data_number_concat[1, 17], 2),
        'C80二次灌浆_风机': round_up(data_number_concat[0, 18], 2), 'C80二次灌浆_风机numbers': round_up(data_number_concat[1, 18], 2)
        }
print(Dict)
docx_box = ['CR_chapter8_template', 'result_chapter8']
save_path = r'C:\Users\Administrator\PycharmProjects\Odoo_addons_NB\autocrword\models\chapter_8'
readpath = os.path.join(save_path, '%s.docx') % docx_box[0]
savepath = os.path.join(save_path, '%s.docx') % docx_box[1]
tpl = DocxTemplate(readpath)
tpl.render(Dict)
tpl.save(savepath)
