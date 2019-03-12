import pandas as pd
import numpy as np
from RoundUp import round_up, round_dict_numbers
from docxtpl import DocxTemplate
import math, os


class RoadBasementDatabase:
    def __init__(self):
        self.earth_excavation_1, self.stone_excavation_1, self.earthwork_backfill_1 = 0, 0, 0
        self.earth_excavation_2, self.stone_excavation_2, self.earthwork_backfill_2 = 0, 0, 0
        self.earth_excavation_3, self.stone_excavation_3, self.earthwork_backfill_3 = 0, 0, 0
        self.earth_excavation_4, self.stone_excavation_4, self.earthwork_backfill_4 = 0, 0, 0
        self.earth_excavation_numbers_1 = 0
        self.road_basic_earthwork_ratio, self.road_basic_stone_ratio = 0, 0
        self.data_1 = pd.DataFrame()
        self.data_2 = pd.DataFrame()
        self.data_3 = pd.DataFrame()
        self.data_4 = pd.DataFrame()
        self.data_timesnumber = pd.DataFrame()
        self.numbers, self.bridge_3, self.grade, self.capacity, self.slope_area, self.terrain_type = 0, 0, 0, 0, 0, []

    def extraction_data(self, terrain_type):
        self.terrain_type = terrain_type
        col_name_1 = ['terrain_type', 'Gradedgravelpavement_1', 'roundtubeculvert_1', 'Stonemasonrydrainageditch_1',
                      'mortarstoneretainingwall_1', 'Turfslopeprotection_1']
        col_name_2 = ['terrain_type', 'Gradedgravelbase_2', 'C30concretepavement_2', 'roundtubeculvert_2',
                      'Stonemasonrydrainageditch_2', 'mortarstoneretainingwall_2', 'Turfslopeprotection_2', 'Signage_2',
                      'Waveguardrail_2']
        col_name_3 = ['terrain_type', 'Mountainpavement_3', 'C30concretepavement_3', 'roundtubeculvert_3',
                      'Stonemasonrydrainageditch_3', 'mortarstoneretainingwall_3', 'Turfslopeprotection_3', 'Signage_3',
                      'Waveguardrail_3', 'Landuse_3']
        col_name_4 = ['terrain_type', 'Generalsiteleveling_4', 'Stonemasonrydrainageditch_4',
                      'mortarstoneprotectionslope_4', 'Turfslopeprotection_4']

        Data_1 = pd.read_excel(
            r'C:\Users\Administrator\PycharmProjects\Odoo_addons_NB\autocrword\models\chapter_8\chapter8database.xlsx',
            header=2, sheet_name='道路基础数据1', usecols=col_name_1)
        Data_2 = pd.read_excel(
            r'C:\Users\Administrator\PycharmProjects\Odoo_addons_NB\autocrword\models\chapter_8\chapter8database.xlsx',
            header=2, sheet_name='道路基础数据2', usecols=col_name_2)
        Data_3 = pd.read_excel(
            r'C:\Users\Administrator\PycharmProjects\Odoo_addons_NB\autocrword\models\chapter_8\chapter8database.xlsx',
            header=2, sheet_name='道路基础数据3', usecols=col_name_3)
        Data_4 = pd.read_excel(
            r'C:\Users\Administrator\PycharmProjects\Odoo_addons_NB\autocrword\models\chapter_8\chapter8database.xlsx',
            header=2, sheet_name='道路基础数据4', usecols=col_name_4)

        self.data_1 = Data_1.loc[Data_1['terrain_type'] == self.terrain_type]
        self.data_2 = Data_2.loc[Data_2['terrain_type'] == self.terrain_type]
        self.data_3 = Data_3.loc[Data_3['terrain_type'] == self.terrain_type]
        self.data_4 = Data_4.loc[Data_4['terrain_type'] == self.terrain_type]
        return self.data_1, self.data_2, self.data_3, self.data_4

    def excavation_cal(self, terrain_type, road_basic_earthwork_ratio, road_basic_stone_ratio, data1, data2, data3,
                       data4):
        self.terrain_type = terrain_type
        self.road_basic_earthwork_ratio = road_basic_earthwork_ratio
        self.road_basic_stone_ratio = road_basic_stone_ratio
        self.data_1 = data1
        self.data_2 = data2
        self.data_3 = data3
        self.data_4 = data4

        if self.terrain_type == '平原':
            self.earth_excavation_1 = self.road_basic_earthwork_ratio * 2.5 * 1000 * 0.4
            self.stone_excavation_1 = self.road_basic_stone_ratio * 2.5 * 1000 * 0.4
            self.earthwork_backfill_1 = 2.5 * 1000 * 0.4
            self.earth_excavation_2 = self.road_basic_earthwork_ratio * 6500 * 0.3
            self.stone_excavation_2 = self.road_basic_stone_ratio * 6500 * 0.3
            self.earthwork_backfill_2 = 6.5 * 1000 * 0.5
            self.earth_excavation_4 = self.road_basic_earthwork_ratio * self.data_4['Generalsiteleveling_4'] * 0.2
            self.stone_excavation_4 = self.road_basic_stone_ratio * self.data_4['Generalsiteleveling_4'] * 0.2
            self.earthwork_backfill_4 = self.data_4['Generalsiteleveling_4'] * 0.2
        elif self.terrain_type == '丘陵':
            self.earth_excavation_1 = self.road_basic_earthwork_ratio * 2.5 * 1000 * 0.4
            self.stone_excavation_1 = self.road_basic_stone_ratio * 2.5 * 1000 * 0.4
            self.earthwork_backfill_1 = 2.5 * 1000 * 0.4
            self.earth_excavation_2 = self.road_basic_earthwork_ratio * 6000
            self.stone_excavation_2 = self.road_basic_stone_ratio * 6000
            self.earthwork_backfill_2 = 6 * 1000 * 0.5
            self.earth_excavation_4 = self.road_basic_earthwork_ratio * self.data_4['Generalsiteleveling_4'] * 2
            self.stone_excavation_4 = self.road_basic_stone_ratio * self.data_4['Generalsiteleveling_4'] * 2
            self.earthwork_backfill_4 = self.data_4['Generalsiteleveling_4'] * 1
        elif self.terrain_type == '缓坡低山':
            self.earth_excavation_1 = self.road_basic_earthwork_ratio * 2.5 * 1000 * 1
            self.stone_excavation_1 = self.road_basic_stone_ratio * 2.5 * 1000 * 1
            self.earthwork_backfill_1 = 2.5 * 1000 * 0.5
            self.earth_excavation_2 = self.road_basic_earthwork_ratio * 8000
            self.stone_excavation_2 = self.road_basic_stone_ratio * 8000
            self.earthwork_backfill_2 = 8 * 1000 * 0.5
            self.earth_excavation_4 = self.road_basic_earthwork_ratio * self.data_4['Generalsiteleveling_4'] * 2
            self.stone_excavation_4 = self.road_basic_stone_ratio * self.data_4['Generalsiteleveling_4'] * 2
            self.earthwork_backfill_4 = self.data_4['Generalsiteleveling_4'] * 1
        elif self.terrain_type == '陡坡低山':
            self.earth_excavation_1 = self.road_basic_earthwork_ratio * 2.5 * 1000 * 2
            self.stone_excavation_1 = self.road_basic_stone_ratio * 2.5 * 1000 * 2
            self.earthwork_backfill_1 = 2.5 * 1000 * 0.5
            self.earth_excavation_2 = self.road_basic_earthwork_ratio * 15000
            self.stone_excavation_2 = self.road_basic_stone_ratio * 15000
            self.earthwork_backfill_2 = 15 * 1000 * 0.3
            self.earth_excavation_4 = self.road_basic_earthwork_ratio * self.data_4['Generalsiteleveling_4'] * 3
            self.stone_excavation_4 = self.road_basic_stone_ratio * self.data_4['Generalsiteleveling_4'] * 3
            self.earthwork_backfill_4 = self.data_4['Generalsiteleveling_4'] * 0.5
        elif self.terrain_type == '缓坡中山':
            self.earth_excavation_1 = self.road_basic_earthwork_ratio * 2.5 * 1000 * 1.5
            self.stone_excavation_1 = self.road_basic_stone_ratio * 2.5 * 1000 * 1.5
            self.earthwork_backfill_1 = 2.5 * 1000 * 0.5
            self.earth_excavation_2 = self.road_basic_earthwork_ratio * 10000
            self.stone_excavation_2 = self.road_basic_stone_ratio * 10000
            self.earthwork_backfill_2 = 10 * 1000 * 0.5
            self.earth_excavation_4 = self.road_basic_earthwork_ratio * self.data_4['Generalsiteleveling_4'] * 2.5
            self.stone_excavation_4 = self.road_basic_stone_ratio * self.data_4['Generalsiteleveling_4'] * 2.5
            self.earthwork_backfill_4 = self.data_4['Generalsiteleveling_4'] * 1
        elif self.terrain_type == '陡坡中山':
            self.earth_excavation_1 = self.road_basic_earthwork_ratio * 2.5 * 1000 * 2.5
            self.stone_excavation_1 = self.road_basic_stone_ratio * 2.5 * 1000 * 2.5
            self.earthwork_backfill_1 = 2.5 * 1000 * 0.5
            self.earth_excavation_2 = self.road_basic_earthwork_ratio * 18000
            self.stone_excavation_2 = self.road_basic_stone_ratio * 18000
            self.earthwork_backfill_2 = 18 * 1000 * 0.3
            self.earth_excavation_4 = self.road_basic_earthwork_ratio * self.data_4['Generalsiteleveling_4'] * 3.5
            self.stone_excavation_4 = self.road_basic_stone_ratio * self.data_4['Generalsiteleveling_4'] * 3.5
            self.earthwork_backfill_4 = self.data_4['Generalsiteleveling_4'] * 0.5
        elif self.terrain_type == '缓坡高山':
            self.earth_excavation_1 = self.road_basic_earthwork_ratio * 2.5 * 1000 * 2
            self.stone_excavation_1 = self.road_basic_stone_ratio * 2.5 * 1000 * 2
            self.earthwork_backfill_1 = 2.5 * 1000 * 0.5
            self.earth_excavation_2 = self.road_basic_earthwork_ratio * 12000
            self.stone_excavation_2 = self.road_basic_stone_ratio * 12000
            self.earthwork_backfill_2 = 12 * 1000 * 0.5
            self.earth_excavation_4 = self.road_basic_earthwork_ratio * self.data_4['Generalsiteleveling_4'] * 2.5
            self.stone_excavation_4 = self.road_basic_stone_ratio * self.data_4['Generalsiteleveling_4'] * 2.5
            self.earthwork_backfill_4 = self.data_4['Generalsiteleveling_4'] * 1
        elif self.terrain_type == '陡坡高山':
            self.earth_excavation_1 = self.road_basic_earthwork_ratio * 2.5 * 1000 * 3
            self.stone_excavation_1 = self.road_basic_stone_ratio * 2.5 * 1000 * 3
            self.earthwork_backfill_1 = 2.5 * 1000 * 0.5
            self.earth_excavation_2 = self.road_basic_earthwork_ratio * 20000
            self.stone_excavation_2 = self.road_basic_stone_ratio * 20000
            self.earthwork_backfill_2 = 20 * 1000 * 0.3
            self.earth_excavation_4 = self.road_basic_earthwork_ratio * self.data_4['Generalsiteleveling_4'] * 4
            self.stone_excavation_4 = self.road_basic_stone_ratio * self.data_4['Generalsiteleveling_4'] * 4
            self.earthwork_backfill_4 = self.data_4['Generalsiteleveling_4'] * 0.5

        self.data_1['Earthexcavation_1'] = self.earth_excavation_1
        self.data_1['Stoneexcavation_1'] = self.stone_excavation_1
        self.data_1['Earthworkbackfill_1'] = self.earthwork_backfill_1

        self.data_2['Earthexcavation_2'] = self.earth_excavation_2
        self.data_2['Stoneexcavation_2'] = self.stone_excavation_2
        self.data_2['Earthworkbackfill_2'] = self.earthwork_backfill_2

        self.data_3['Earthexcavation_3'] = self.earth_excavation_2
        self.data_3['Stoneexcavation_3'] = self.stone_excavation_2
        self.data_3['Earthworkbackfill_3'] = self.earthwork_backfill_2
        self.data_3['bridge_3'] = self.bridge_3

        self.data_4['Earthexcavation_4'] = self.earth_excavation_4
        self.data_4['Stoneexcavation_4'] = self.stone_excavation_4
        self.data_4['Earthworkbackfill_4'] = self.earthwork_backfill_4

        return self.data_1, self.data_2, self.data_3, self.data_4

    def generate_dict(self, data1, data2, data3, data4, numbers_list):
        self.data_1 = data1
        self.data_2 = data2
        self.data_3 = data3
        self.data_4 = data4
        self.numbers_list = numbers_list
        dict_road_base_1 = {
            'numbers_1': self.numbers_list[0],
            '土方开挖_1': self.data_1.at[self.data_1.index[0], 'Earthexcavation_1'],
            '石方开挖_1': self.data_1.at[self.data_1.index[0], 'Stoneexcavation_1'],
            '土石方回填_1': self.data_1.at[self.data_1.index[0], 'Earthworkbackfill_1'],
            '山皮石路面_1': self.data_1.at[self.data_1.index[0], 'Gradedgravelpavement_1'],
            '圆管涵_1': self.data_1.at[self.data_1.index[0], 'roundtubeculvert_1'],
            '浆砌石排水沟_1': self.data_1.at[self.data_1.index[0], 'Stonemasonrydrainageditch_1'],
            '浆砌片石挡墙_1': self.data_1.at[self.data_1.index[0], 'mortarstoneretainingwall_1'],
            '草皮护坡_1': self.data_1.at[self.data_1.index[0], 'Turfslopeprotection_1'],
        }
        dict_road_base_2 = {
            'numbers_2': self.numbers_list[1],
            '土方开挖_2': self.data_2.at[self.data_2.index[0], 'Earthexcavation_2'],
            '石方开挖_2': self.data_2.at[self.data_2.index[0], 'Stoneexcavation_2'],
            '土石方回填_2': self.data_2.at[self.data_2.index[0], 'Earthworkbackfill_2'],
            '级配碎石基层_2': self.data_2.at[self.data_2.index[0], 'Gradedgravelbase_2'],
            'C30混凝土路面_2': self.data_2.at[self.data_2.index[0], 'C30concretepavement_2'],
            '圆管涵_2': self.data_2.at[self.data_2.index[0], 'roundtubeculvert_2'],
            '浆砌石排水沟_2': self.data_2.at[self.data_2.index[0], 'Stonemasonrydrainageditch_2'],
            '浆砌片石挡墙_2': self.data_2.at[self.data_2.index[0], 'mortarstoneretainingwall_2'],
            '草皮护坡_2': self.data_2.at[self.data_2.index[0], 'Turfslopeprotection_2'],
            '标志标牌_2': self.data_2.at[self.data_2.index[0], 'Signage_2'],
            '波形护栏_2': self.data_2.at[self.data_2.index[0], 'Waveguardrail_2'],
        }
        dict_road_base_3 = {
            'numbers_3': self.numbers_list[2],
            '土方开挖_3': self.data_3.at[self.data_3.index[0], 'Earthexcavation_3'],
            '石方开挖_3': self.data_3.at[self.data_3.index[0], 'Stoneexcavation_3'],
            '土石方回填_3': self.data_3.at[self.data_3.index[0], 'Earthworkbackfill_3'],
            '山皮石路面_3': self.data_3.at[self.data_3.index[0], 'Mountainpavement_3'],
            'C30混凝土路面_3': self.data_3.at[self.data_3.index[0], 'C30concretepavement_3'],
            '圆管涵_3': self.data_3.at[self.data_3.index[0], 'roundtubeculvert_3'],
            '浆砌石排水沟_3': self.data_3.at[self.data_3.index[0], 'Stonemasonrydrainageditch_3'],
            '浆砌片石挡墙_3': self.data_3.at[self.data_3.index[0], 'mortarstoneretainingwall_3'],
            '草皮护坡_3': self.data_3.at[self.data_3.index[0], 'Turfslopeprotection_3'],
            '标志标牌_3': self.data_3.at[self.data_3.index[0], 'Signage_3'],
            '波形护栏_3': self.data_3.at[self.data_3.index[0], 'Waveguardrail_3'],
            '桥梁_3': self.data_3.at[self.data_3.index[0], 'bridge_3'],
        }

        dict_road_base_4 = {
            'numbers_4': self.numbers_list[3],
            '浆砌片石护坡_4': self.data_4.at[self.data_4.index[0], 'mortarstoneprotectionslope_4'],
            '一般场地平整_4': self.data_4.at[self.data_4.index[0], 'Generalsiteleveling_4'],
            '土方开挖_4': self.data_4.at[self.data_4.index[0], 'Earthexcavation_4'],
            '石方开挖_4': self.data_4.at[self.data_4.index[0], 'Stoneexcavation_4'],
            '土石方回填_4': self.data_4.at[self.data_4.index[0], 'Earthworkbackfill_4'],
            '浆砌石排水沟_4': self.data_4.at[self.data_4.index[0], 'Stonemasonrydrainageditch_4'],
        }
        return dict_road_base_1, dict_road_base_2, dict_road_base_3, dict_road_base_4


numberslist = [5, 1.5, 10, 15]
project04 = RoadBasementDatabase()
data_1, data_2, data_3, data_4 = project04.extraction_data('陡坡低山')
data_cal, data_ca2, data_ca3, data_ca4 = project04.excavation_cal('陡坡低山', 0.8, 0.2, data_1, data_2, data_3, data_4)
dict_road_base_1, dict_road_base_2, dict_road_base_3, dict_road_base_4 = project04.generate_dict(data_cal, data_ca2,
                                                                                                 data_ca3, data_ca4,
                                                                                                 numberslist)
Dict_1 = round_dict_numbers(dict_road_base_1, dict_road_base_1['numbers_1'])
Dict_2 = round_dict_numbers(dict_road_base_2, dict_road_base_2['numbers_2'])
Dict_3 = round_dict_numbers(dict_road_base_3, dict_road_base_3['numbers_3'])
Dict_4 = round_dict_numbers(dict_road_base_4, dict_road_base_4['numbers_4'])
Dict = dict(Dict_1, **Dict_2, **Dict_3, **Dict_4)

print(Dict)
print("=======================")
filename_box = ['cr8', 'result_chapter8']
save_path = r'C:\Users\Administrator\PycharmProjects\Odoo_addons_NB\autocrword\models\chapter_8'
read_path = os.path.join(save_path, '%s.docx') % filename_box[0]
save_path = os.path.join(save_path, '%s.docx') % filename_box[1]
tpl = DocxTemplate(read_path)
tpl.render(Dict)
tpl.save(save_path)
print("==========finished=============")
