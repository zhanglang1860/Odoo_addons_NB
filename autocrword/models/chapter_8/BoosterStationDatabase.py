import pandas as pd
import numpy as np
from RoundUp import round_up, round_dict
from docxtpl import DocxTemplate
import math, os


class BoosterStationDatabase:
    def __init__(self):
        self.status, self.earth_excavation_booster_station, self.stone_excavation_booster_station, self.earthwork_backfill_booster_station = 0, 0, 0, 0
        self.road_basic_earthwork_ratio, self.road_basic_stone_ratio = 0, 0
        self.data = 0
        self.grade, self.capacity, self.slope_area, self.terrain_type = 0, 0, 0, []
        self.DataBoosterStation, self.data_booster_station = pd.DataFrame(), pd.DataFrame()

    def extraction_data_booster_station(self, status, grade, capacity):
        self.status = status
        self.grade = grade
        self.capacity = capacity
        col_name = ['Status', 'Grade', 'Capacity', 'Long', 'Width', 'InnerWallArea', 'WallLength', 'StoneMasonryFoot',
                    'StoneMasonryDrainageDitch', 'RoadArea', 'GreenArea', 'ComprehensiveBuilding', 'EquipmentBuilding',
                    'AffiliatedBuilding', 'C30Concrete', 'C15ConcreteCushion', 'MainTransformerFoundation',
                    'AccidentOilPoolC30Concrete', 'AccidentOilPoolC15Cushion', 'AccidentOilPoolReinforcement',
                    'FoundationC25Concrete', 'OutdoorStructure', 'PrecastConcretePole', 'LightningRod'
                    ]

        self.DataBoosterStation = pd.read_excel(
            r'C:\Users\Administrator\PycharmProjects\Odoo_addons_NB\autocrword\models\chapter_8\chapter8database.xlsx',
            header=2, sheet_name='升压站基础数据', usecols=col_name)

        self.data_booster_station = self.DataBoosterStation.loc[self.DataBoosterStation['Status'] == self.status].loc[
            self.DataBoosterStation['Grade'] == self.grade].loc[self.DataBoosterStation['Capacity'] == self.capacity]

        return self.data_booster_station

    def excavation_cal_booster_station(self, data_booster_station, road_basic_earthwork_ratio, road_basic_stone_ratio,
                                       terrain_type):
        self.data_booster_station = data_booster_station
        self.road_basic_earthwork_ratio = road_basic_earthwork_ratio
        self.road_basic_stone_ratio = road_basic_stone_ratio
        self.terrain_type = terrain_type

        if self.terrain_type == '平原':
            self.slope_area = (self.data_booster_station['Long'] + 5) * (self.data_booster_station['Width'] + 5)
            self.earth_excavation_booster_station = self.slope_area * 0.3 * self.road_basic_earthwork_ratio / 10
            self.stone_excavation_booster_station = self.slope_area * 0.3 * self.road_basic_stone_ratio / 10
            self.earthwork_backfill_booster_station = self.slope_area * 2
        else:
            self.slope_area = (self.data_booster_station['Long'] + 10) * (self.data_booster_station['Width'] + 10)
            self.earth_excavation_booster_station = self.slope_area * 3 * self.road_basic_earthwork_ratio
            self.stone_excavation_booster_station = self.slope_area * 3 * self.road_basic_stone_ratio
            self.earthwork_backfill_booster_station = self.slope_area * 0.5

        self.data_booster_station['Earthexcavation_BoosterStation'] = self.earth_excavation_booster_station
        self.data_booster_station['Stoneexcavation_BoosterStation'] = self.stone_excavation_booster_station
        self.data_booster_station['Earthworkbackfill_BoosterStation'] = self.earthwork_backfill_booster_station
        self.data_booster_station['slope_area'] = self.slope_area

        return self.data_booster_station

    def generate_dict(self, data):
        self.data = data
        print(self.data)
        dict_booster_station = {'变电站围墙内面积': self.data.at[self.data.index[0], 'Innerwallarea'],
                                '含放坡面积': self.data.at[self.data.index[0], 'slope_area'],
                                '道路面积': self.data.at[self.data.index[0], 'Roadarea'],
                                '围墙长度': self.data.at[self.data.index[0], 'Walllength'],
                                '绿化面积': self.data.at[self.data.index[0], 'Greenarea'],
                                '土方开挖_升压站': self.data.at[self.data.index[0], 'Earthexcavation'],
                                '综合楼': self.data.at[self.data.index[0], 'Comprehensivebuilding'],
                                '石方开挖_升压站': self.data.at[self.data.index[0], 'Stoneexcavation'],
                                '设备楼': self.data.at[self.data.index[0], 'Equipmentbuilding'],
                                '土方回填_升压站': self.data.at[self.data.index[0], 'Earthworkbackfill'],
                                '附属楼': self.data.at[self.data.index[0], 'Affiliatedbuilding'],
                                '浆砌石护脚': self.data.at[self.data.index[0], 'Stonemasonryfoot'],
                                '主变基础C3self.data.index[0]混凝土': self.data.at[self.data.index[0], 'C30concrete'],
                                '浆砌石排水沟': self.data.at[self.data.index[0], 'Stonemasonrydrainageditch'],
                                'C15混凝土垫层': self.data.at[self.data.index[0], 'C15concretecushion'],
                                '主变压器基础钢筋': self.data.at[self.data.index[0], 'Maintransformerfoundation'],
                                '事故油池C15垫层': self.data.at[self.data.index[0], 'AccidentoilpoolC15cushion'],
                                '事故油池C3self.data.index[0]混凝土': self.data.at[
                                    self.data.index[0], 'AccidentoilpoolC30concrete'],
                                '事故油池钢筋': self.data.at[self.data.index[0], 'Accidentoilpoolreinforcement'],
                                '设备及架构基础C25混凝土': self.data.at[self.data.index[0], 'FoundationC25Concrete'],
                                '室外架构': self.data.at[self.data.index[0], 'Outdoorstructure'],
                                '预制混凝土杆': self.data.at[self.data.index[0], 'Precastconcretepole'],
                                '避雷针': self.data.at[self.data.index[0], 'lightningrod'], }
        return dict_booster_station


project03 = BoosterStationDatabase()
data = project03.extraction_data('新建', 110, 100)
data_cal = project03.excavation_cal(0.8, 0.2, '平原')

Dict = round_dict(project03.generate_dict(data_cal))
print(Dict)
filename_box = ['cr8', 'result_chapter8']
save_path = r'C:\Users\Administrator\PycharmProjects\Odoo_addons_NB\autocrword\models\chapter_8'
read_path = os.path.join(save_path, '%s.docx') % filename_box[0]
save_path = os.path.join(save_path, '%s.docx') % filename_box[1]
tpl = DocxTemplate(read_path)
tpl.render(Dict)
tpl.save(save_path)
