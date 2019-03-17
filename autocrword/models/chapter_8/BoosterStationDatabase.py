import pandas as pd


# import numpy as np
# from RoundUp import round_up, round_dict
# from docxtpl import DocxTemplate
# import math, os

class BoosterStationDatabase:
    def __init__(self):
        # ===========selecting parameters=============
        self.Status, self.Grade, self.Capacity = 0, 0, 0
        # ===========basic parameters==============
        self.DataBoosterStation, self.data_booster_station = pd.DataFrame(), pd.DataFrame()
        self.road_basic_earthwork_ratio, self.road_basic_stone_ratio, self.TerrainType = 0, 0, []
        self.dict_booster_station = {}
        # ===========Calculated parameters==============
        self.slope_area, self.earth_excavation_booster_station, self.stone_excavation_booster_station = 0, 0, 0
        self.earthwork_back_fill_booster_station, self.c30_booster_station, self.c15_booster_station = 0, 0, 0
        self.c15_oil_pool_booster_station, self.c30_oil_pool_booster_station = 0, 0
        self.c25_foundation_booster_station, self.reinforcement_booster_station = 0, 0

    def extraction_data_booster_station(self, status, grade, capacity):
        self.Status = status
        self.Grade = grade
        self.Capacity = capacity
        col_name = ['Status', 'Grade', 'Capacity', 'Long', 'Width', 'InnerWallArea', 'WallLength', 'StoneMasonryFoot',
                    'StoneMasonryDrainageDitch', 'RoadArea', 'GreenArea', 'ComprehensiveBuilding', 'EquipmentBuilding',
                    'AffiliatedBuilding', 'C30Concrete', 'C15ConcreteCushion', 'MainTransformerFoundation',
                    'AccidentOilPoolC30Concrete', 'AccidentOilPoolC15Cushion', 'AccidentOilPoolReinforcement',
                    'FoundationC25Concrete', 'OutdoorStructure', 'PrecastConcretePole', 'LightningRod'
                    ]

        self.DataBoosterStation = pd.read_excel(
            r'C:\Users\Administrator\PycharmProjects\Odoo_addons_NB\autocrword\models\chapter_8\chapter8database.xlsx',
            header=2, sheet_name='升压站基础数据', usecols=col_name)

        self.data_booster_station = self.DataBoosterStation.loc[self.DataBoosterStation['Status'] == self.Status].loc[
            self.DataBoosterStation['Grade'] == self.Grade].loc[self.DataBoosterStation['Capacity'] == self.Capacity]

        return self.data_booster_station

    def excavation_cal_booster_station(self, data_booster_station, road_basic_earthwork_ratio, road_basic_stone_ratio,
                                       terrain_type):
        self.data_booster_station = data_booster_station
        self.road_basic_earthwork_ratio = road_basic_earthwork_ratio
        self.road_basic_stone_ratio = road_basic_stone_ratio
        self.TerrainType = terrain_type

        if self.TerrainType == '平原':
            self.slope_area = (self.data_booster_station['Long'] + 5) * (self.data_booster_station['Width'] + 5)
            self.earth_excavation_booster_station = self.slope_area * 0.3 * self.road_basic_earthwork_ratio / 10
            self.stone_excavation_booster_station = self.slope_area * 0.3 * self.road_basic_stone_ratio / 10
            self.earthwork_back_fill_booster_station = self.slope_area * 2
        else:
            self.slope_area = (self.data_booster_station['Long'] + 10) * (self.data_booster_station['Width'] + 10)
            self.earth_excavation_booster_station = self.slope_area * 3 * self.road_basic_earthwork_ratio
            self.stone_excavation_booster_station = self.slope_area * 3 * self.road_basic_stone_ratio
            self.earthwork_back_fill_booster_station = self.slope_area * 0.5

        self.c30_booster_station = self.data_booster_station.at[self.data_booster_station.index[0], 'C30Concrete']

        self.c15_booster_station = \
            self.data_booster_station.at[self.data_booster_station.index[0], 'C15ConcreteCushion']

        self.c15_oil_pool_booster_station = \
            self.data_booster_station.at[self.data_booster_station.index[0], 'AccidentOilPoolC15Cushion']

        self.c30_oil_pool_booster_station = \
            self.data_booster_station.at[self.data_booster_station.index[0], 'AccidentOilPoolC30Concrete']

        self.c25_foundation_booster_station = \
            self.data_booster_station.at[self.data_booster_station.index[0], 'FoundationC25Concrete']

        self.reinforcement_booster_station = \
            self.data_booster_station.at[self.data_booster_station.index[0], 'MainTransformerFoundation'] + \
            self.data_booster_station.at[self.data_booster_station.index[0], 'AccidentOilPoolReinforcement'] + \
            self.data_booster_station.at[self.data_booster_station.index[0], 'LightningRod']

        self.data_booster_station['EarthExcavation_BoosterStation'] = self.earth_excavation_booster_station
        self.data_booster_station['StoneExcavation_BoosterStation'] = self.stone_excavation_booster_station
        self.data_booster_station['EarthWorkBackFill_BoosterStation'] = self.earthwork_back_fill_booster_station
        self.data_booster_station['SlopeArea'] = self.slope_area

        return self.data_booster_station

    def generate_dict_booster_station(self, data_booster_station):
        self.data_booster_station = data_booster_station
        self.dict_booster_station = {
            '变电站围墙内面积': self.data_booster_station.at[self.data_booster_station.index[0], 'InnerWallArea'],
            '含放坡面积': self.data_booster_station.at[self.data_booster_station.index[0], 'SlopeArea'],
            '道路面积': self.data_booster_station.at[self.data_booster_station.index[0], 'RoadArea'],
            '围墙长度': self.data_booster_station.at[self.data_booster_station.index[0], 'WallLength'],
            '绿化面积': self.data_booster_station.at[self.data_booster_station.index[0], 'GreenArea'],
            '土方开挖_升压站': self.data_booster_station.at[
                self.data_booster_station.index[0], 'EarthExcavation_BoosterStation'],
            '综合楼': self.data_booster_station.at[self.data_booster_station.index[0], 'ComprehensiveBuilding'],
            '石方开挖_升压站': self.data_booster_station.at[
                self.data_booster_station.index[0], 'StoneExcavation_BoosterStation'],
            '设备楼': self.data_booster_station.at[self.data_booster_station.index[0], 'EquipmentBuilding'],
            '土方回填_升压站': self.data_booster_station.at[
                self.data_booster_station.index[0], 'EarthWorkBackFill_BoosterStation'],
            '附属楼': self.data_booster_station.at[self.data_booster_station.index[0], 'AffiliatedBuilding'],
            '浆砌石护脚': self.data_booster_station.at[self.data_booster_station.index[0], 'StoneMasonryFoot'],
            '主变基础C30混凝土': self.data_booster_station.at[self.data_booster_station.index[0], 'C30Concrete'],
            '浆砌石排水沟': self.data_booster_station.at[self.data_booster_station.index[0], 'StoneMasonryDrainageDitch'],
            'C15混凝土垫层': self.data_booster_station.at[self.data_booster_station.index[0], 'C15ConcreteCushion'],
            '主变压器基础钢筋': self.data_booster_station.at[self.data_booster_station.index[0], 'MainTransformerFoundation'],
            '事故油池C15垫层': self.data_booster_station.at[self.data_booster_station.index[0], 'AccidentOilPoolC15Cushion'],
            '事故油池C30混凝土': self.data_booster_station.at[
                self.data_booster_station.index[0], 'AccidentOilPoolC30Concrete'],
            '事故油池钢筋': self.data_booster_station.at[self.data_booster_station.index[0], 'AccidentOilPoolReinforcement'],
            '设备及架构基础C25混凝土': self.data_booster_station.at[self.data_booster_station.index[0], 'FoundationC25Concrete'],
            '室外架构': self.data_booster_station.at[self.data_booster_station.index[0], 'OutdoorStructure'],
            '预制混凝土杆': self.data_booster_station.at[self.data_booster_station.index[0], 'PrecastConcretePole'],
            '避雷针': self.data_booster_station.at[self.data_booster_station.index[0], 'LightningRod'], }
        return self.dict_booster_station

#
# project03 = BoosterStationDatabase()
# data = project03.extraction_data_booster_station('新建', 110, 100)
# data_cal = project03.excavation_cal_booster_station(data,0.8, 0.2, '陡坡低山')
#
# Dict = round_dict(project03.generate_dict_booster_station(data_cal))
# print(Dict)
# filename_box = ['cr8', 'result_chapter8']
# save_path = r'C:\Users\Administrator\PycharmProjects\Odoo_addons_NB\autocrword\models\chapter_8'
# read_path = os.path.join(save_path, '%s.docx') % filename_box[0]
# save_path = os.path.join(save_path, '%s.docx') % filename_box[1]
# tpl = DocxTemplate(read_path)
# tpl.render(Dict)
# tpl.save(save_path)
