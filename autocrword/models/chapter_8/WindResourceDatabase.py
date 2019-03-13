import pandas as pd
import math, os
from docxtpl import DocxTemplate
from RoundUp import round_dict_numbers


class WindResourceDatabase:

    def __init__(self):
        self.BasicType, self.FortificationIntensity, self.UltimateLoad = '', 0, 0
        self.numbers_list, self.dict_wind_resource, self.basic_earthwork_ratio, self.basic_stone_ratio = [], {}, 0, 0
        self.earth_excavation_tur, self.stone_excavation_tur, self.earth_work_back_fill_tur = 0, 0, 0
        self.data_wind_resource = pd.DataFrame()
        self.DataTurbine = pd.DataFrame()

    def extraction_data_turbine(self, fortification_intensity, basic_type, ultimate_load):
        self.FortificationIntensity = fortification_intensity
        self.BasicType = basic_type
        self.UltimateLoad = ultimate_load
        col_name = ['FortificationIntensity', 'BearingCapacity', 'BasicType', 'UltimateLoad', 'FloorRadiusR', 'R1',
                    'R2', 'H1', 'H2', 'H3', 'PileDiameter', 'Number', 'Length', 'SinglePileLength', 'Area', 'Volume',
                    'Cushion', 'M48PreStressedAnchor', 'C80SecondaryGrouting']

        self.DataTurbine = pd.read_excel(
            r'C:\Users\Administrator\PycharmProjects\Odoo_addons_NB\autocrword\models\chapter_8\chapter8database.xlsx',
            header=1, sheet_name='风机基础数据', usecols=col_name)
        self.data_wind_resource = \
            self.DataTurbine.loc[self.DataTurbine['FortificationIntensity'] == self.FortificationIntensity].loc[
                self.DataTurbine['BasicType'] == self.BasicType].loc[
                self.DataTurbine['UltimateLoad'] == self.UltimateLoad]
        return self.data_wind_resource

    def excavation_cal_turbine(self, data_wind_resource, basic_earthwork_ratio, basic_stone_ratio, numbers_list):
        self.data_wind_resource = data_wind_resource
        self.basic_earthwork_ratio = basic_earthwork_ratio
        self.basic_stone_ratio = basic_stone_ratio
        self.earth_excavation_tur = math.pi * (self.data_wind_resource['FloorRadiusR'] + 1.3) ** 2 * (
                self.data_wind_resource['H1'] + self.data_wind_resource['H2'] + self.data_wind_resource[
            'H3'] + 0.15) * self.basic_earthwork_ratio

        self.stone_excavation_tur = math.pi * (self.data_wind_resource['FloorRadiusR'] + 1.3) ** 2 * (
                self.data_wind_resource['H1'] + self.data_wind_resource['H2'] + self.data_wind_resource[
            'H3'] + 0.15) * self.basic_stone_ratio

        self.earth_work_back_fill_tur = self.earth_excavation_tur + self.stone_excavation_tur - self.data_wind_resource[
            'Volume'] - self.data_wind_resource['Cushion']

        self.data_wind_resource['EarthExcavation_Turbine'] = self.earth_excavation_tur
        self.data_wind_resource['StoneExcavation_Turbine'] = self.stone_excavation_tur
        self.data_wind_resource['EarthWorkBackFill_Turbine'] = self.earth_work_back_fill_tur

        self.data_wind_resource['EarthExcavation_Turbine_Numbers'] = self.earth_excavation_tur * numbers_list[0]
        self.data_wind_resource['StoneExcavation_Turbine_Numbers'] = self.stone_excavation_tur * numbers_list[0]
        self.data_wind_resource['EarthWorkBackFill_Turbine_Numbers'] = self.earth_work_back_fill_tur * numbers_list[0]

        self.data_wind_resource['Reinforcement'] = self.data_wind_resource['Volume'] * 0.1
        return self.data_wind_resource

    def generate_dict_turbine(self, data, numbers_list):
        self.data_wind_resource = data
        self.numbers_list = numbers_list
        self.dict_wind_resource = {
            'numbers_tur': int(self.numbers_list[0]),
            '土方开挖_风机': self.data_wind_resource.at[self.data_wind_resource.index[0], 'EarthExcavation_Turbine'],
            '石方开挖_风机': self.data_wind_resource.at[self.data_wind_resource.index[0], 'StoneExcavation_Turbine'],
            '土石方回填_风机': self.data_wind_resource.at[self.data_wind_resource.index[0], 'EarthWorkBackFill_Turbine'],
            'C40混凝土_风机': self.data_wind_resource.at[self.data_wind_resource.index[0], 'Volume'],
            'C15混凝土_风机': self.data_wind_resource.at[self.data_wind_resource.index[0], 'Cushion'],
            '钢筋_风机': self.data_wind_resource.at[self.data_wind_resource.index[0], 'Reinforcement'],
            '基础防水_风机': 1,
            '沉降观测_风机': 4,
            '预制桩长_风机': self.data_wind_resource.at[self.data_wind_resource.index[0], 'SinglePileLength'],
            'M48预应力锚栓_风机': self.data_wind_resource.at[self.data_wind_resource.index[0], 'M48PreStressedAnchor'],
            'C80二次灌浆_风机': self.data_wind_resource.at[self.data_wind_resource.index[0], 'C80SecondaryGrouting'],
        }
        return self.dict_wind_resource


project01 = WindResourceDatabase()
data = project01.extraction_data_turbine(basic_type='扩展基础', ultimate_load=70000, fortification_intensity=7)
numbers_list = [15]
data_cal = project01.excavation_cal_turbine(0.8, 0.2, numbers_list)
dict_wind_resource = project01.generate_dict_turbine(data_cal, numbers_list)
Dict = round_dict_numbers(dict_wind_resource, dict_wind_resource['numbers_tur'])

docx_box = ['cr8', 'result_chapter8']
save_path = r'C:\Users\Administrator\PycharmProjects\Odoo_addons_NB\autocrword\models\chapter_8'
readpath = os.path.join(save_path, '%s.docx') % docx_box[0]
savepath = os.path.join(save_path, '%s.docx') % docx_box[1]
tpl = DocxTemplate(readpath)
tpl.render(Dict)
tpl.save(savepath)
