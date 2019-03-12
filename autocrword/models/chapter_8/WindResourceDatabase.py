import pandas as pd
import math, os
from docxtpl import DocxTemplate
import numpy as np
from RoundUp import round_up,round_dict_numbers


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
            Data['Basictype'] == self.Basictype].loc[Data['Ultimateload'] == self.Ultimateload]
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

        self.data['Earthexcavation_tur'] = self.earth_excavation
        self.data['Stoneexcavation_tur'] = self.stone_excavation
        self.data['Earthworkbackfill_tur'] = self.earthwork_backfill
        self.data['Reinforcement'] = self.data['Volume'] * 0.1
        return self.data

    def generate_dict(self, data, numbers_list):
        self.data = data
        self.numbers_list = numbers_list
        dict_wind_resource = {
            'numbers_tur': int(self.numbers_list[0]),
            '土方开挖_风机': self.data.at[self.data.index[0], 'Earthexcavation_tur'],
            '石方开挖_风机': self.data.at[self.data.index[0], 'Stoneexcavation_tur'],
            '土石方回填_风机': self.data.at[self.data.index[0], 'Earthworkbackfill_tur'],
            'C40混凝土_风机': self.data.at[self.data.index[0], 'Volume'],
            'C15混凝土_风机': self.data.at[self.data.index[0], 'Cushion'],
            '钢筋_风机': self.data.at[self.data.index[0], 'Reinforcement'],
            '基础防水_风机': 1,
            '沉降观测_风机': 4,
            '预制桩长_风机': self.data.at[self.data.index[0], 'Singlepilelength'],
            'M48预应力锚栓_风机': self.data.at[self.data.index[0], 'M48PrestressedAnchor'],
            'C80二次灌浆_风机': self.data.at[self.data.index[0], 'C80secondarygrouting'],
        }
        return dict_wind_resource


project01 = WindResourceDatabase()
data = project01.extraction_data(Basictype='扩展基础', Ultimateload=70000, Fortificationintensity=7)
numbers_list = [15]
data_cal = project01.excavation_cal(0.8, 0.2)
dict_wind_resource = project01.generate_dict(data_cal, numbers_list)
Dict = round_dict_numbers(dict_wind_resource, dict_wind_resource['numbers_tur'])
print(Dict)
docx_box = ['cr8', 'result_chapter8']
save_path = r'C:\Users\Administrator\PycharmProjects\Odoo_addons_NB\autocrword\models\chapter_8'
readpath = os.path.join(save_path, '%s.docx') % docx_box[0]
savepath = os.path.join(save_path, '%s.docx') % docx_box[1]
tpl = DocxTemplate(readpath)
tpl.render(Dict)
tpl.save(savepath)
