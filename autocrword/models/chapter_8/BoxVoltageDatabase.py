import pandas as pd
import numpy as np
from RoundUp import round_up
from docxtpl import DocxTemplate
import math, os


class BoxVoltageDatabase:
    def __init__(self):
        self.earth_excavation_box_voltage, self.stone_excavation_box_voltage, self.earthwork_back_fill_box_voltage = 0, 0, 0
        self.TurbineCapacity, self.road_earthwork_ratio, self.road_stone_ratio = 0, 0, 0
        self.DataBoxVoltage, self.data_box_voltage = pd.DataFrame(), pd.DataFrame()

    def extraction_data(self, turbine_capacity):
        self.TurbineCapacity = turbine_capacity
        col_name = ['TurbineCapacity', 'ConvertStation', 'Long', 'Width', 'High', 'WallThickness', 'HighPressure',
                    'C35ConcreteTop', 'C15Cushion', 'MU10Brick', 'Reinforcement', 'Area']
        self.DataBoxVoltage = pd.read_excel(
            r'C:\Users\Administrator\PycharmProjects\Odoo_addons_NB\autocrword\models\chapter_8\chapter8database.xlsx',
            header=2, sheet_name='箱变基础数据', usecols=col_name)
        self.data_box_voltage = self.DataBoxVoltage.loc[self.DataBoxVoltage['TurbineCapacity'] == self.TurbineCapacity]
        return self.data_box_voltage

    def excavation_cal(self, road_earthwork_ratio, road_stone_ratio):
        self.road_earthwork_ratio = road_earthwork_ratio
        self.road_stone_ratio = road_stone_ratio
        self.earth_excavation_box_voltage = (self.data_box_voltage['Long'] + 0.5 * 2) * (
                self.data_box_voltage['Width'] + 0.5 * 2) * (
                                                    self.data_box_voltage['High'] - 0.2) * self.road_earthwork_ratio
        self.stone_excavation_box_voltage = (self.data_box_voltage['Long'] + 0.5 * 2) * (
                self.data_box_voltage['Width'] + 0.5 * 2) * (
                                                    self.data_box_voltage['High'] - 0.2) * self.road_stone_ratio
        self.earthwork_back_fill_box_voltage = self.earth_excavation_box_voltage + self.stone_excavation_box_voltage - \
                                               self.data_box_voltage['long'] * self.data_box_voltage[
                                                   'width'] * (self.data_box_voltage['high'] - 0.2)
        self.data_box_voltage['EarthExcavation_BoxVoltage'] = self.earth_excavation_box_voltage
        self.data_box_voltage['StoneExcavation_BoxVoltage'] = self.stone_excavation_box_voltage
        self.data_box_voltage['EarthworkBackFill_BoxVoltage'] = self.earthwork_back_fill_box_voltage
        return self.data_box_voltage

    def generate_dict(self, data, numbers_list):
        self.data_box_voltage = data
        self.numbers_list = numbers_list
        dict_wind_resource = {
            'numbers_tur': int(self.numbers_list[0]),
            '土方开挖_风机': self.data_box_voltage.at[self.data_box_voltage.index[0], 'EarthExcavation_Turbine'],
            '石方开挖_风机': self.data_box_voltage.at[self.data_box_voltage.index[0], 'StoneExcavation_Turbine'],
            '土石方回填_风机': self.data_box_voltage.at[self.data_box_voltage.index[0], 'EarthWorkBackFill_Turbine'],
            'C40混凝土_风机': self.data_box_voltage.at[self.data_box_voltage.index[0], 'Volume'],
            'C15混凝土_风机': self.data_box_voltage.at[self.data_box_voltage.index[0], 'Cushion'],
            '钢筋_风机': self.data_box_voltage.at[self.data_box_voltage.index[0], 'Reinforcement'],
            '基础防水_风机': 1,
            '沉降观测_风机': 4,
            '预制桩长_风机': self.data_box_voltage.at[self.data_box_voltage.index[0], 'SinglePileLength'],
            'M48预应力锚栓_风机': self.data_box_voltage.at[self.data_box_voltage.index[0], 'M48PreStressedAnchor'],
            'C80二次灌浆_风机': self.data_box_voltage.at[self.data_box_voltage.index[0], 'C80SecondaryGrouting'],
        }
        return dict_wind_resource


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
