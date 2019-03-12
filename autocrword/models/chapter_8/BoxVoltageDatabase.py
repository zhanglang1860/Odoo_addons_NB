import pandas as pd
import numpy as np
from RoundUp import round_up
from docxtpl import DocxTemplate
import math, os


class BoxVoltageDatabase:
    def __init__(self):
        self.Turbinecapacity, self.earth_excavation, self.stone_excavation, self.earthwork_backfill = 0, 0, 0, 0
        self.road_basic_earthwork_ratio, road_basic_stone_ratio = 0, 0
        self.data = 0
        self.data_timesnumber = pd.DataFrame()

    def extraction_data(self, Turbinecapacity):
        self.Turbinecapacity = Turbinecapacity

        col_name = ['Turbinecapacity', 'convertingstation', 'long', 'width', 'high', 'Wallthickness', 'Highpressure',
                    'C35concretetop', 'C15cushion', 'MU10brick', 'Reinforcement', 'area']

        Data = pd.read_excel(
            r'C:\Users\Administrator\PycharmProjects\Odoo_addons_NB\autocrword\models\chapter_8\chapter8database.xlsx',
            header=2, sheet_name='箱变基础数据', usecols=col_name)
        self.data = Data.loc[Data['Turbinecapacity'] == self.Turbinecapacity]
        return self.data

    def excavation_cal(self, road_basic_earthwork_ratio, road_basic_stone_ratio):
        self.road_basic_earthwork_ratio = road_basic_earthwork_ratio
        self.road_basic_stone_ratio = road_basic_stone_ratio
        self.earth_excavation = (self.data['long'] + 0.5 * 2) * (self.data['width'] + 0.5 * 2) * (
                self.data['high'] - 0.2) * self.road_basic_earthwork_ratio
        self.stone_excavation = (self.data['long'] + 0.5 * 2) * (self.data['width'] + 0.5 * 2) * (
                self.data['high'] - 0.2) * self.road_basic_stone_ratio
        self.earthwork_backfill = self.earth_excavation + self.stone_excavation - self.data['long'] * self.data[
            'width'] * (self.data['high'] - 0.2)
        self.data['Earthexcavation'] = self.earth_excavation
        self.data['Stoneexcavation'] = self.stone_excavation
        self.data['Earthworkbackfill'] = self.earthwork_backfill
        return self.data

    def data_numbers_cal(self, num):
        self.numbers = num
        for i in range(0, self.data.shape[1]):
            # print(self.data.iloc[:, i].dtype)
            if self.data.iloc[:, i].dtype != 'object':
                self.data_timesnumber.at[0, i] = self.data.iloc[0, i] * self.numbers
            else:
                self.data_timesnumber.at[0, i] = self.data.iloc[0, i]
        self.data_timesnumber_np = np.array(self.data_timesnumber)
        self.data_np = np.array(self.data)
        self.data_number_concat_np = np.vstack([self.data_np, self.data_timesnumber_np])
        np.set_printoptions(suppress=True)
        return self.data_number_concat_np


numbers = 20
project02 = BoxVoltageDatabase()
data = project02.extraction_data(3)
data_cal = project02.excavation_cal(0.8, 0.2)
data_number_concat = project02.data_numbers_cal(20)

Dict = {'numbers': numbers,
        '土方开挖_箱变': round_up(data_number_concat[0, 12], 2), '土方开挖_箱变numbers': round_up(data_number_concat[1, 12], 2),
        '石方开挖_箱变': round_up(data_number_concat[0, 13], 2), '石方开挖_箱变numbers': round_up(data_number_concat[1, 13], 2),
        '土石方回填_箱变': round_up(data_number_concat[0, 14], 2), '土石方回填_箱变numbers': round_up(data_number_concat[1, 14], 2),
        'C35混凝土_箱变': round_up(data_number_concat[0, 7], 2), 'C35混凝土_箱变numbers': round_up(data_number_concat[1, 7], 2),
        'C15混凝土_箱变': round_up(data_number_concat[0, 8], 2), 'C15混凝土_箱变numbers': round_up(data_number_concat[1, 8], 2),
        'MU10砖_箱变': round_up(data_number_concat[0, 9], 2), 'MU10砖_箱变numbers': round_up(data_number_concat[1, 9], 2),
        '钢筋_箱变': round_up(data_number_concat[0, 10], 2), '钢筋_箱变numbers': round_up(data_number_concat[1, 10], 2)
        }
print(Dict)
docx_box = ['CR_chapter8_template', 'result_chapter8']
save_path = r'C:\Users\Administrator\PycharmProjects\Odoo_addons_NB\autocrword\models\chapter_8'
readpath = os.path.join(save_path, '%s.docx') % docx_box[0]
savepath = os.path.join(save_path, '%s.docx') % docx_box[1]
tpl = DocxTemplate(readpath)
tpl.render(Dict)
tpl.save(savepath)


# earth_excavation, stone_excavation, earthwork_backfill = project02.excavation_cal(0.8, 0.2)

# data['Earthexcavation'] = earth_excavation
# data['Stoneexcavation'] = stone_excavation
# data['Earthworkbackfill'] = earthwork_backfill
# print(data['Earthexcavation'])
