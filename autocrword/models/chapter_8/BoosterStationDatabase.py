import pandas as pd
import numpy as np
from RoundUp import round_up
from docxtpl import DocxTemplate
import math, os


class BoosterStationDatabase:
    def __init__(self):
        self.status, self.earth_excavation, self.stone_excavation, self.earthwork_backfill = 0, 0, 0, 0
        self.basic_earthwork_ratio, self.basic_stone_ratio = 0, 0
        self.data = 0
        self.data_timesnumber = pd.DataFrame()
        self.grade, self.capacity, self.slope_area, self.terrain_type = 0, 0, 0, []

    def extraction_data(self, status, grade, capacity):
        self.status = status
        self.grade = grade
        self.capacity = capacity
        col_name = ['status', 'grade', 'capacity', 'long', 'width', 'Innerwallarea', 'Walllength', 'Stonemasonryfoot',
                    'Stonemasonrydrainageditch', 'Roadarea', 'Greenarea', 'Comprehensivebuilding', 'Equipmentbuilding',
                    'Affiliatedbuilding', 'C30concrete', 'C15concretecushion', 'Maintransformerfoundation',
                    'AccidentoilpoolC30concrete', 'AccidentoilpoolC15cushion', 'Accidentoilpoolreinforcement',
                    'FoundationC25Concrete', 'Outdoorstructure', 'Precastconcretepole', 'lightningrod'
                    ]

        Data = pd.read_excel(
            r'C:\Users\Administrator\PycharmProjects\Odoo_addons_NB\autocrword\models\chapter_8\chapter8database.xlsx',
            header=2, sheet_name='升压站基础数据', usecols=col_name)

        self.data = Data.loc[Data['status'] == self.status].loc[Data['grade'] == self.grade].loc[
            Data['capacity'] == self.capacity]
        return self.data

    def excavation_cal(self, basic_earthwork_ratio, basic_stone_ratio, terrain_type):
        self.basic_earthwork_ratio = basic_earthwork_ratio
        self.basic_stone_ratio = basic_stone_ratio
        self.terrain_type = terrain_type

        if self.terrain_type == ['平原']:
            self.slope_area = (self.data['long'] + 5) * (self.data['width'] + 5)
            self.earth_excavation = self.slope_area * 0.3 * self.basic_earthwork_ratio / 10
            self.stone_excavation = self.slope_area * 0.3 * self.basic_stone_ratio / 10
            self.earthwork_backfill = self.slope_area * 2
        else:
            self.slope_area = (self.data['long'] + 10) * (self.data['width'] + 10)
            self.earth_excavation = self.slope_area * 3 * self.basic_earthwork_ratio
            self.stone_excavation = self.slope_area * 3 * self.basic_stone_ratio
            self.earthwork_backfill = self.slope_area * 0.5

        self.data['Earthexcavation'] = self.earth_excavation
        self.data['Stoneexcavation'] = self.stone_excavation
        self.data['Earthworkbackfill'] = self.earthwork_backfill
        self.data['slope_area'] = self.slope_area
        print(self.data['Earthexcavation'])
        return self.data

    def generate_dict(self, data):
        self.data = data
        print(self.data)
        dict_booster_station = {'变电站围墙内面积': self.data.at[0, 'Innerwallarea'],
                                '含放坡面积': self.data.at[0, 'slope_area'], '道路面积': self.data.at[0, 'Roadarea'],
                                '围墙长度': self.data.at[0, 'Walllength'], '绿化面积': self.data.at[0, 'Greenarea'],
                                '土方开挖_升压站': self.data.at[0, 'Earthexcavation'],
                                '综合楼': self.data.at[0, 'Comprehensivebuilding'],
                                '石方开挖_升压站': self.data.at[0, 'Stoneexcavation'],
                                '设备楼': self.data.at[0, 'Equipmentbuilding'],
                                '土方回填_升压站': self.data.at[0, 'Earthworkbackfill'],
                                '附属楼': self.data.at[0, 'Affiliatedbuilding'],
                                '浆砌石护脚': self.data.at[0, 'Stonemasonryfoot'],
                                '主变基础C30混凝土': self.data.at[0, 'C30concrete'],
                                '浆砌石排水沟': self.data.at[0, 'Stonemasonrydrainageditch'],
                                'C15混凝土垫层': self.data.at[0, 'C15concretecushion'],
                                '主变压器基础钢筋': self.data.at[0, 'Maintransformerfoundation'],
                                '事故油池C15垫层': self.data.at[0, 'AccidentoilpoolC15cushion'],
                                '事故油池C30混凝土': self.data.at[0, 'AccidentoilpoolC30concrete'],
                                '事故油池钢筋': self.data.at[0, 'Accidentoilpoolreinforcement'],
                                '设备及架构基础C25混凝土': self.data.at[0, 'FoundationC25Concrete'],
                                '室外架构': self.data.at[0, 'Outdoorstructure'],
                                '预制混凝土杆': self.data.at[0, 'Precastconcretepole'],
                                '避雷针': self.data.at[0, 'lightningrod'], }
        return dict_booster_station


project03 = BoosterStationDatabase()
data = project03.extraction_data('新建', 110, 50)
data_cal = project03.excavation_cal(0.8, 0.2, '丘陵')

Dict = project03.generate_dict(data_cal)
print(Dict)
filename_box = ['CR_chapter8_template', 'result_chapter8']
save_path = r'C:\Users\Administrator\PycharmProjects\Odoo_addons_NB\autocrword\models\chapter_8'
read_path = os.path.join(save_path, '%s.docx') % filename_box[0]
save_path = os.path.join(save_path, '%s.docx') % filename_box[1]
tpl = DocxTemplate(read_path)
tpl.render(Dict)
tpl.save(save_path)
