import pandas as pd
import numpy as np
from RoundUp import round_up
from docxtpl import DocxTemplate
import math, os


class RoadBasementDatabase:
    def __init__(self):
        self.status, self.earth_excavation, self.stone_excavation, self.earthwork_backfill = 0, 0, 0, 0
        self.road_basic_earthwork_ratio, self.road_basic_stone_ratio = 0, 0
        self.data = pd.DataFrame()
        self.data_timesnumber = pd.DataFrame()
        self.grade, self.capacity, self.slope_area, self.terrain_type = 0, 0, 0, []

    def extraction_data_1(self, terrain_type):
        self.terrain_type = terrain_type
        col_name = ['terrain_type', 'Gradedgravelpavement', 'roundtubeculvert', 'Stonemasonrydrainageditch',
                    'mortarstoneretainingwall', 'Turfslopeprotection'
                    ]

        Data = pd.read_excel(
            r'C:\Users\Administrator\PycharmProjects\Odoo_addons_NB\autocrword\models\chapter_8\chapter8database.xlsx',
            header=2, sheet_name='道路基础数据1', usecols=col_name)

        self.data_1 = Data.loc[Data['terrain_type'] == self.terrain_type]
        return self.data_1

    def excavation_cal_1(self, road_basic_earthwork_ratio, road_basic_stone_ratio):
        self.road_basic_earthwork_ratio = road_basic_earthwork_ratio
        self.road_basic_stone_ratio = road_basic_stone_ratio

        self.earth_excavation_1 = self.road_basic_earthwork_ratio * 2.5 * 1000 * 0.4
        self.stone_excavation_1 = self.road_basic_stone_ratio * 2.5 * 1000 * 0.4
        self.earthwork_backfill_1 = 2.5 * 1000 * 0.4

        self.data_1['Earthexcavation_1'] = self.earth_excavation_1
        self.data_1['Stoneexcavation_1'] = self.stone_excavation_1
        self.data_1['Earthworkbackfill_1'] = self.earthwork_backfill_1
        return self.data_1




    def excavation_cal_2(self, road_basic_earthwork_ratio, road_basic_stone_ratio):
        self.road_basic_earthwork_ratio = road_basic_earthwork_ratio
        self.road_basic_stone_ratio = road_basic_stone_ratio

        self.earth_excavation_1 = self.road_basic_earthwork_ratio * 2.5 * 1000 * 0.4
        self.stone_excavation_1 = self.road_basic_stone_ratio * 2.5 * 1000 * 0.4
        self.earthwork_backfill_1 = 2.5 * 1000 * 0.4

        self.data['Earthexcavation_1'] = self.earth_excavation_1
        self.data['Stoneexcavation_1'] = self.stone_excavation_1
        self.data['Earthworkbackfill_1'] = self.earthwork_backfill_1
        return self.data


    def generate_dict(self, data):
        self.data = data
        print(self.data)
        dict_booster_station = {'土方开挖_1': self.data.at[0, 'Earthexcavation_1'],
                                '石方开挖_1': self.data.at[0, 'Stoneexcavation_1'], '道路面积': self.data.at[0, 'Roadarea'],
                                '土石方回填_1': self.data.at[0, 'Earthworkbackfill_1'], '绿化面积': self.data.at[0, 'Greenarea'],
                                '山皮石路面': self.data.at[0, 'Gradedgravelpavement'],
                                '圆管涵': self.data.at[0, 'roundtubeculvert'],
                                '浆砌石排水沟_1': self.data.at[0, 'Stonemasonrydrainageditch'],
                                '浆砌片石挡墙': self.data.at[0, 'mortarstoneretainingwall'],
                                '草皮护坡': self.data.at[0, 'Turfslopeprotection'],
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
