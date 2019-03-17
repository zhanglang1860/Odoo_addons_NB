import pandas as pd


# import numpy as np
# from RoundUp import round_up, round_dict_numbers
# from docxtpl import DocxTemplate
# import math, os


class RoadBasementDatabase:
    def __init__(self):
        # ===========selecting parameters=============
        self.TerrainType = ''
        # ===========basic parameters==============
        self.DataRoadBasement_1, self.DataRoadBasement_2 = pd.DataFrame(), pd.DataFrame()
        self.DataRoadBasement_3, self.DataRoadBasement_4 = pd.DataFrame(), pd.DataFrame()
        self.data_road_base_1, self.data_road_base_2 = pd.DataFrame(), pd.DataFrame()
        self.data_road_base_3, self.data_road_base_4 = pd.DataFrame(), pd.DataFrame()
        self.road_basic_earthwork_ratio, self.road_basic_stone_ratio = 0, 0
        self.KM_list = []
        # ===========Calculated parameters==============
        self.earth_road_base_excavation_1, self.stone_road_base_excavation_1 = 0, 0
        self.earth_road_base_excavation_2, self.stone_road_base_excavation_2 = 0, 0
        self.earth_road_base_excavation_3, self.stone_road_base_excavation_3 = 0, 0
        self.earth_road_base_excavation_4, self.stone_road_base_excavation_4 = 0, 0
        self.earthwork_road_base_back_fill_1, self.earthwork_road_base_back_fill_2 = 0, 0
        self.earthwork_road_base_back_fill_3, self.earthwork_road_base_back_fill_4 = 0, 0

        self.earth_road_base_excavation_1_numbers, self.stone_road_base_excavation_1_numbers = 0, 0
        self.earthwork_road_base_back_fill_1_numbers, self.StoneMasonryDrainageDitch_1_numbers = 0, 0
        self.earth_road_base_excavation_2_numbers, self.stone_road_base_excavation_2_numbers = 0, 0
        self.earthwork_road_base_back_fill_2_numbers, self.StoneMasonryDrainageDitch_2_numbers = 0, 0
        self.earth_road_base_excavation_3_numbers, self.stone_road_base_excavation_3_numbers = 0, 0
        self.earthwork_road_base_back_fill_3_numbers, self.StoneMasonryDrainageDitch_3_numbers = 0, 0
        self.earth_road_base_excavation_4_numbers, self.stone_road_base_excavation_4_numbers = 0, 0
        self.earthwork_road_base_back_fill_4_numbers, self.StoneMasonryDrainageDitch_4_numbers = 0, 0
        self.MortarStoneRetainingWall_1_numbers, self.MortarStoneRetainingWall_2_numbers = 0, 0
        self.MortarStoneRetainingWall_3_numbers, self.MortarStoneRetainingWall_4_numbers = 0, 0
        self.c30_road_base_1_numbers, self.c30_road_base_2_numbers = 0, 0
        self.c30_road_base_3_numbers, self.c30_road_base_4_numbers = 0, 0

    def extraction_data_road_basement(self, terrain_type):
        self.TerrainType = terrain_type
        col_name_1 = ['TerrainType', 'GradedGravelPavement_1', 'RoundTubeCulvert_1', 'StoneMasonryDrainageDitch_1',
                      'MortarStoneRetainingWall_1', 'TurfSlopeProtection_1']
        col_name_2 = ['TerrainType', 'GradedGravelBase_2', 'C30ConcretePavement_2', 'RoundTubeCulvert_2',
                      'StoneMasonryDrainageDitch_2', 'MortarStoneRetainingWall_2', 'TurfSlopeProtection_2', 'Signage_2',
                      'WaveGuardrail_2']
        col_name_3 = ['TerrainType', 'MountainPavement_3', 'C30ConcretePavement_3', 'RoundTubeCulvert_3',
                      'StoneMasonryDrainageDitch_3', 'MortarStoneRetainingWall_3', 'TurfSlopeProtection_3', 'Signage_3',
                      'WaveGuardrail_3', 'LandUse_3']
        col_name_4 = ['TerrainType', 'GeneralSiteLeveling_4', 'StoneMasonryDrainageDitch_4',
                      'MortarStoneProtectionSlope_4', 'TurfSlopeProtection_4']

        self.DataRoadBasement_1 = pd.read_excel(
            r'C:\Users\Administrator\PycharmProjects\Odoo_addons_NB\autocrword\models\chapter_8\chapter8database.xlsx',
            header=2, sheet_name='道路基础数据1', usecols=col_name_1)
        self.DataRoadBasement_2 = pd.read_excel(
            r'C:\Users\Administrator\PycharmProjects\Odoo_addons_NB\autocrword\models\chapter_8\chapter8database.xlsx',
            header=2, sheet_name='道路基础数据2', usecols=col_name_2)
        self.DataRoadBasement_3 = pd.read_excel(
            r'C:\Users\Administrator\PycharmProjects\Odoo_addons_NB\autocrword\models\chapter_8\chapter8database.xlsx',
            header=2, sheet_name='道路基础数据3', usecols=col_name_3)
        self.DataRoadBasement_4 = pd.read_excel(
            r'C:\Users\Administrator\PycharmProjects\Odoo_addons_NB\autocrword\models\chapter_8\chapter8database.xlsx',
            header=2, sheet_name='道路基础数据4', usecols=col_name_4)

        self.data_road_base_1 = self.DataRoadBasement_1.loc[self.DataRoadBasement_1['TerrainType'] == self.TerrainType]
        self.data_road_base_2 = self.DataRoadBasement_2.loc[self.DataRoadBasement_2['TerrainType'] == self.TerrainType]
        self.data_road_base_3 = self.DataRoadBasement_3.loc[self.DataRoadBasement_3['TerrainType'] == self.TerrainType]
        self.data_road_base_4 = self.DataRoadBasement_4.loc[self.DataRoadBasement_4['TerrainType'] == self.TerrainType]
        return self.data_road_base_1, self.data_road_base_2, self.data_road_base_3, self.data_road_base_4

    def excavation_cal_road_basement(self, data1, data2, data3, data4, road_basic_earthwork_ratio,
                                     road_basic_stone_ratio, terrain_type, km_li):
        self.TerrainType = terrain_type
        self.road_basic_earthwork_ratio = road_basic_earthwork_ratio
        self.road_basic_stone_ratio = road_basic_stone_ratio
        self.data_road_base_1, self.data_road_base_2 = data1, data2
        self.data_road_base_3, self.data_road_base_4 = data3, data4
        self.KM_list = km_li

        if self.TerrainType == '平原':
            self.earth_road_base_excavation_1 = self.road_basic_earthwork_ratio * 2.5 * 1000 * 0.4
            self.stone_road_base_excavation_1 = self.road_basic_stone_ratio * 2.5 * 1000 * 0.4
            self.earthwork_road_base_back_fill_1 = 2.5 * 1000 * 0.4
            self.earth_road_base_excavation_2 = self.road_basic_earthwork_ratio * 6500 * 0.3
            self.stone_road_base_excavation_2 = self.road_basic_stone_ratio * 6500 * 0.3
            self.earthwork_road_base_back_fill_2 = 6.5 * 1000 * 0.5
            self.earth_road_base_excavation_4 = self.road_basic_earthwork_ratio * self.data_road_base_4[
                'GeneralSiteLeveling_4'] * 0.2
            self.stone_road_base_excavation_4 = self.road_basic_stone_ratio * self.data_road_base_4[
                'GeneralSiteLeveling_4'] * 0.2
            self.earthwork_road_base_back_fill_4 = self.data_road_base_4['GeneralSiteLeveling_4'] * 0.2
        elif self.TerrainType == '丘陵':
            self.earth_road_base_excavation_1 = self.road_basic_earthwork_ratio * 2.5 * 1000 * 0.4
            self.stone_road_base_excavation_1 = self.road_basic_stone_ratio * 2.5 * 1000 * 0.4
            self.earthwork_road_base_back_fill_1 = 2.5 * 1000 * 0.4
            self.earth_road_base_excavation_2 = self.road_basic_earthwork_ratio * 6000
            self.stone_road_base_excavation_2 = self.road_basic_stone_ratio * 6000
            self.earthwork_road_base_back_fill_2 = 6 * 1000 * 0.5
            self.earth_road_base_excavation_4 = self.road_basic_earthwork_ratio * self.data_road_base_4[
                'GeneralSiteLeveling_4'] * 2
            self.stone_road_base_excavation_4 = self.road_basic_stone_ratio * self.data_road_base_4[
                'GeneralSiteLeveling_4'] * 2
            self.earthwork_road_base_back_fill_4 = self.data_road_base_4['GeneralSiteLeveling_4'] * 1
        elif self.TerrainType == '缓坡低山':
            self.earth_road_base_excavation_1 = self.road_basic_earthwork_ratio * 2.5 * 1000 * 1
            self.stone_road_base_excavation_1 = self.road_basic_stone_ratio * 2.5 * 1000 * 1
            self.earthwork_road_base_back_fill_1 = 2.5 * 1000 * 0.5
            self.earth_road_base_excavation_2 = self.road_basic_earthwork_ratio * 8000
            self.stone_road_base_excavation_2 = self.road_basic_stone_ratio * 8000
            self.earthwork_road_base_back_fill_2 = 8 * 1000 * 0.5
            self.earth_road_base_excavation_4 = self.road_basic_earthwork_ratio * self.data_road_base_4[
                'GeneralSiteLeveling_4'] * 2
            self.stone_road_base_excavation_4 = self.road_basic_stone_ratio * self.data_road_base_4[
                'GeneralSiteLeveling_4'] * 2
            self.earthwork_road_base_back_fill_4 = self.data_road_base_4['GeneralSiteLeveling_4'] * 1
        elif self.TerrainType == '陡坡低山':
            self.earth_road_base_excavation_1 = self.road_basic_earthwork_ratio * 2.5 * 1000 * 2
            self.stone_road_base_excavation_1 = self.road_basic_stone_ratio * 2.5 * 1000 * 2
            self.earthwork_road_base_back_fill_1 = 2.5 * 1000 * 0.5
            self.earth_road_base_excavation_2 = self.road_basic_earthwork_ratio * 15000
            self.stone_road_base_excavation_2 = self.road_basic_stone_ratio * 15000
            self.earthwork_road_base_back_fill_2 = 15 * 1000 * 0.3
            self.earth_road_base_excavation_4 = self.road_basic_earthwork_ratio * self.data_road_base_4[
                'GeneralSiteLeveling_4'] * 3
            self.stone_road_base_excavation_4 = self.road_basic_stone_ratio * self.data_road_base_4[
                'GeneralSiteLeveling_4'] * 3
            self.earthwork_road_base_back_fill_4 = self.data_road_base_4['GeneralSiteLeveling_4'] * 0.5
        elif self.TerrainType == '缓坡中山':
            self.earth_road_base_excavation_1 = self.road_basic_earthwork_ratio * 2.5 * 1000 * 1.5
            self.stone_road_base_excavation_1 = self.road_basic_stone_ratio * 2.5 * 1000 * 1.5
            self.earthwork_road_base_back_fill_1 = 2.5 * 1000 * 0.5
            self.earth_road_base_excavation_2 = self.road_basic_earthwork_ratio * 10000
            self.stone_road_base_excavation_2 = self.road_basic_stone_ratio * 10000
            self.earthwork_road_base_back_fill_2 = 10 * 1000 * 0.5
            self.earth_road_base_excavation_4 = self.road_basic_earthwork_ratio * self.data_road_base_4[
                'GeneralSiteLeveling_4'] * 2.5
            self.stone_road_base_excavation_4 = self.road_basic_stone_ratio * self.data_road_base_4[
                'GeneralSiteLeveling_4'] * 2.5
            self.earthwork_road_base_back_fill_4 = self.data_road_base_4['GeneralSiteLeveling_4'] * 1
        elif self.TerrainType == '陡坡中山':
            self.earth_road_base_excavation_1 = self.road_basic_earthwork_ratio * 2.5 * 1000 * 2.5
            self.stone_road_base_excavation_1 = self.road_basic_stone_ratio * 2.5 * 1000 * 2.5
            self.earthwork_road_base_back_fill_1 = 2.5 * 1000 * 0.5
            self.earth_road_base_excavation_2 = self.road_basic_earthwork_ratio * 18000
            self.stone_road_base_excavation_2 = self.road_basic_stone_ratio * 18000
            self.earthwork_road_base_back_fill_2 = 18 * 1000 * 0.3
            self.earth_road_base_excavation_4 = self.road_basic_earthwork_ratio * self.data_road_base_4[
                'GeneralSiteLeveling_4'] * 3.5
            self.stone_road_base_excavation_4 = self.road_basic_stone_ratio * self.data_road_base_4[
                'GeneralSiteLeveling_4'] * 3.5
            self.earthwork_road_base_back_fill_4 = self.data_road_base_4['GeneralSiteLeveling_4'] * 0.5
        elif self.TerrainType == '缓坡高山':
            self.earth_road_base_excavation_1 = self.road_basic_earthwork_ratio * 2.5 * 1000 * 2
            self.stone_road_base_excavation_1 = self.road_basic_stone_ratio * 2.5 * 1000 * 2
            self.earthwork_road_base_back_fill_1 = 2.5 * 1000 * 0.5
            self.earth_road_base_excavation_2 = self.road_basic_earthwork_ratio * 12000
            self.stone_road_base_excavation_2 = self.road_basic_stone_ratio * 12000
            self.earthwork_road_base_back_fill_2 = 12 * 1000 * 0.5
            self.earth_road_base_excavation_4 = self.road_basic_earthwork_ratio * self.data_road_base_4[
                'GeneralSiteLeveling_4'] * 2.5
            self.stone_road_base_excavation_4 = self.road_basic_stone_ratio * self.data_road_base_4[
                'GeneralSiteLeveling_4'] * 2.5
            self.earthwork_road_base_back_fill_4 = self.data_road_base_4['GeneralSiteLeveling_4'] * 1
        elif self.TerrainType == '陡坡高山':
            self.earth_road_base_excavation_1 = self.road_basic_earthwork_ratio * 2.5 * 1000 * 3
            self.stone_road_base_excavation_1 = self.road_basic_stone_ratio * 2.5 * 1000 * 3
            self.earthwork_road_base_back_fill_1 = 2.5 * 1000 * 0.5
            self.earth_road_base_excavation_2 = self.road_basic_earthwork_ratio * 20000
            self.stone_road_base_excavation_2 = self.road_basic_stone_ratio * 20000
            self.earthwork_road_base_back_fill_2 = 20 * 1000 * 0.3
            self.earth_road_base_excavation_4 = self.road_basic_earthwork_ratio * self.data_road_base_4[
                'GeneralSiteLeveling_4'] * 4
            self.stone_road_base_excavation_4 = self.road_basic_stone_ratio * self.data_road_base_4[
                'GeneralSiteLeveling_4'] * 4
            self.earthwork_road_base_back_fill_4 = self.data_road_base_4['GeneralSiteLeveling_4'] * 0.5
        self.earth_road_base_excavation_3 = self.earth_road_base_excavation_2
        self.stone_road_base_excavation_3 = self.stone_road_base_excavation_2
        self.earthwork_road_base_back_fill_3 = self.earthwork_road_base_back_fill_2

        self.earth_road_base_excavation_1_numbers = self.earth_road_base_excavation_1 * self.KM_list[0]
        self.stone_road_base_excavation_1_numbers = self.stone_road_base_excavation_1 * self.KM_list[0]
        self.earthwork_road_base_back_fill_1_numbers = self.earthwork_road_base_back_fill_1 * self.KM_list[0]
        self.StoneMasonryDrainageDitch_1_numbers = \
            self.data_road_base_1.at[self.data_road_base_1.index[0], 'StoneMasonryDrainageDitch_1'] * self.KM_list[0]
        self.MortarStoneRetainingWall_1_numbers = \
            self.data_road_base_1.at[self.data_road_base_1.index[0], 'MortarStoneRetainingWall_1'] * self.KM_list[0]

        self.earth_road_base_excavation_2_numbers = self.earth_road_base_excavation_2 * self.KM_list[1]
        self.stone_road_base_excavation_2_numbers = self.stone_road_base_excavation_2 * self.KM_list[1]
        self.earthwork_road_base_back_fill_2_numbers = self.earthwork_road_base_back_fill_2 * self.KM_list[1]
        self.c30_road_base_2_numbers = \
            self.data_road_base_2.at[self.data_road_base_2.index[0], 'C30ConcretePavement_2'] * self.KM_list[1]
        self.StoneMasonryDrainageDitch_2_numbers = \
            self.data_road_base_2.at[self.data_road_base_2.index[0], 'StoneMasonryDrainageDitch_2'] * self.KM_list[1]
        self.MortarStoneRetainingWall_2_numbers = \
            self.data_road_base_2.at[self.data_road_base_2.index[0], 'MortarStoneRetainingWall_2'] * self.KM_list[1]

        self.earth_road_base_excavation_3_numbers = self.earth_road_base_excavation_3 * self.KM_list[2]
        self.stone_road_base_excavation_3_numbers = self.stone_road_base_excavation_3 * self.KM_list[2]
        self.earthwork_road_base_back_fill_3_numbers = self.earthwork_road_base_back_fill_3 * self.KM_list[2]
        self.c30_road_base_3_numbers = \
            self.data_road_base_3.at[self.data_road_base_3.index[0], 'C30ConcretePavement_3'] * self.KM_list[2]
        self.StoneMasonryDrainageDitch_3_numbers = \
            self.data_road_base_3.at[self.data_road_base_3.index[0], 'StoneMasonryDrainageDitch_3'] * self.KM_list[2]
        self.MortarStoneRetainingWall_3_numbers = \
            self.data_road_base_3.at[self.data_road_base_3.index[0], 'MortarStoneRetainingWall_3'] * self.KM_list[2]

        self.earth_road_base_excavation_4_numbers = self.earth_road_base_excavation_4 * self.KM_list[3]
        self.stone_road_base_excavation_4_numbers = self.stone_road_base_excavation_4 * self.KM_list[3]
        self.earthwork_road_base_back_fill_4_numbers = self.earthwork_road_base_back_fill_4 * self.KM_list[3]
        self.StoneMasonryDrainageDitch_4_numbers = \
            self.data_road_base_4.at[self.data_road_base_4.index[0], 'StoneMasonryDrainageDitch_4'] * self.KM_list[3]
        self.MortarStoneRetainingWall_4_numbers = \
            self.data_road_base_4.at[self.data_road_base_4.index[0], 'MortarStoneProtectionSlope_4'] * self.KM_list[3]

        self.data_road_base_1['EarthExcavation_RoadBase_1'] = self.earth_road_base_excavation_1
        self.data_road_base_1['StoneExcavation_RoadBase_1'] = self.stone_road_base_excavation_1
        self.data_road_base_1['EarthWorkBackFill_RoadBase_1'] = self.earthwork_road_base_back_fill_1

        self.data_road_base_2['EarthExcavation_RoadBase_2'] = self.earth_road_base_excavation_2
        self.data_road_base_2['StoneExcavation_RoadBase_2'] = self.stone_road_base_excavation_2
        self.data_road_base_2['EarthWorkBackFill_RoadBase_2'] = self.earthwork_road_base_back_fill_2

        self.data_road_base_3['EarthExcavation_RoadBase_3'] = self.earth_road_base_excavation_2
        self.data_road_base_3['StoneExcavation_RoadBase_3'] = self.stone_road_base_excavation_2
        self.data_road_base_3['EarthWorkBackFill_RoadBase_3'] = self.earthwork_road_base_back_fill_2
        self.data_road_base_3['Bridge_3'] = 0

        self.data_road_base_4['EarthExcavation_RoadBase_4'] = self.earth_road_base_excavation_4
        self.data_road_base_4['StoneExcavation_RoadBase_4'] = self.stone_road_base_excavation_4
        self.data_road_base_4['EarthWorkBackFill_RoadBase_4'] = self.earthwork_road_base_back_fill_4

        return self.data_road_base_1, self.data_road_base_2, self.data_road_base_3, self.data_road_base_4

    def generate_dict_road_basement(self, data1, data2, data3, data4, km_li):
        self.data_road_base_1, self.data_road_base_2 = data1, data2
        self.data_road_base_3, self.data_road_base_4 = data3, data4
        self.KM_list = km_li
        dict_road_base_1 = {
            'numbers_1': self.KM_list[0],
            '土方开挖_1': self.data_road_base_1.at[self.data_road_base_1.index[0], 'EarthExcavation_RoadBase_1'],
            '石方开挖_1': self.data_road_base_1.at[self.data_road_base_1.index[0], 'StoneExcavation_RoadBase_1'],
            '土石方回填_1': self.data_road_base_1.at[self.data_road_base_1.index[0], 'EarthWorkBackFill_RoadBase_1'],
            '山皮石路面_1': self.data_road_base_1.at[self.data_road_base_1.index[0], 'GradedGravelPavement_1'],
            '圆管涵_1': self.data_road_base_1.at[self.data_road_base_1.index[0], 'RoundTubeCulvert_1'],
            '浆砌石排水沟_1': self.data_road_base_1.at[self.data_road_base_1.index[0], 'StoneMasonryDrainageDitch_1'],
            '浆砌片石挡墙_1': self.data_road_base_1.at[self.data_road_base_1.index[0], 'MortarStoneRetainingWall_1'],
            '草皮护坡_1': self.data_road_base_1.at[self.data_road_base_1.index[0], 'TurfSlopeProtection_1'],
        }
        dict_road_base_2 = {
            'numbers_2': self.KM_list[1],
            '土方开挖_2': self.data_road_base_2.at[self.data_road_base_2.index[0], 'EarthExcavation_RoadBase_2'],
            '石方开挖_2': self.data_road_base_2.at[self.data_road_base_2.index[0], 'StoneExcavation_RoadBase_2'],
            '土石方回填_2': self.data_road_base_2.at[self.data_road_base_2.index[0], 'EarthWorkBackFill_RoadBase_2'],
            '级配碎石基层_2': self.data_road_base_2.at[self.data_road_base_2.index[0], 'GradedGravelBase_2'],
            'C30混凝土路面_2': self.data_road_base_2.at[self.data_road_base_2.index[0], 'C30ConcretePavement_2'],
            '圆管涵_2': self.data_road_base_2.at[self.data_road_base_2.index[0], 'RoundTubeCulvert_2'],
            '浆砌石排水沟_2': self.data_road_base_2.at[self.data_road_base_2.index[0], 'StoneMasonryDrainageDitch_2'],
            '浆砌片石挡墙_2': self.data_road_base_2.at[self.data_road_base_2.index[0], 'MortarStoneRetainingWall_2'],
            '草皮护坡_2': self.data_road_base_2.at[self.data_road_base_2.index[0], 'TurfSlopeProtection_2'],
            '标志标牌_2': self.data_road_base_2.at[self.data_road_base_2.index[0], 'Signage_2'],
            '波形护栏_2': self.data_road_base_2.at[self.data_road_base_2.index[0], 'WaveGuardrail_2'],
        }
        dict_road_base_3 = {
            'numbers_3': self.KM_list[2],
            '土方开挖_3': self.data_road_base_3.at[self.data_road_base_3.index[0], 'EarthExcavation_RoadBase_3'],
            '石方开挖_3': self.data_road_base_3.at[self.data_road_base_3.index[0], 'StoneExcavation_RoadBase_3'],
            '土石方回填_3': self.data_road_base_3.at[self.data_road_base_3.index[0], 'EarthWorkBackFill_RoadBase_3'],
            '山皮石路面_3': self.data_road_base_3.at[self.data_road_base_3.index[0], 'MountainPavement_3'],
            'C30混凝土路面_3': self.data_road_base_3.at[self.data_road_base_3.index[0], 'C30ConcretePavement_3'],
            '圆管涵_3': self.data_road_base_3.at[self.data_road_base_3.index[0], 'RoundTubeCulvert_3'],
            '浆砌石排水沟_3': self.data_road_base_3.at[self.data_road_base_3.index[0], 'StoneMasonryDrainageDitch_3'],
            '浆砌片石挡墙_3': self.data_road_base_3.at[self.data_road_base_3.index[0], 'MortarStoneRetainingWall_3'],
            '草皮护坡_3': self.data_road_base_3.at[self.data_road_base_3.index[0], 'TurfSlopeProtection_3'],
            '标志标牌_3': self.data_road_base_3.at[self.data_road_base_3.index[0], 'Signage_3'],
            '波形护栏_3': self.data_road_base_3.at[self.data_road_base_3.index[0], 'WaveGuardrail_3'],
            '桥梁_3': self.data_road_base_3.at[self.data_road_base_3.index[0], 'Bridge_3'],
        }

        dict_road_base_4 = {
            'numbers_4': self.KM_list[3],
            '浆砌片石护坡_4': self.data_road_base_4.at[self.data_road_base_4.index[0], 'MortarStoneProtectionSlope_4'],
            '一般场地平整_4': self.data_road_base_4.at[self.data_road_base_4.index[0], 'GeneralSiteLeveling_4'],
            '土方开挖_4': self.data_road_base_4.at[self.data_road_base_4.index[0], 'EarthExcavation_RoadBase_4'],
            '石方开挖_4': self.data_road_base_4.at[self.data_road_base_4.index[0], 'StoneExcavation_RoadBase_4'],
            '土石方回填_4': self.data_road_base_4.at[self.data_road_base_4.index[0], 'EarthWorkBackFill_RoadBase_4'],
            '浆砌石排水沟_4': self.data_road_base_4.at[self.data_road_base_4.index[0], 'StoneMasonryDrainageDitch_4'],
        }
        return dict_road_base_1, dict_road_base_2, dict_road_base_3, dict_road_base_4

# numberslist = [5, 1.5, 10, 15]
# project04 = RoadBasementDatabase()
# data_1, data_2, data_3, data_4 = project04.extraction_data_road_basement('陡坡低山')
# data_cal, data_ca2, data_ca3, data_ca4 = \
#     project04.excavation_cal_road_basement(data_1, data_2, data_3, data_4, '陡坡低山', 0.8, 0.2, numberslist)
# dict_road_base_1, dict_road_base_2, dict_road_base_3, dict_road_base_4 = \
#     project04.generate_dict_road_basement(data_cal, data_ca2, data_ca3, data_ca4, numberslist)
# Dict_1 = round_dict_numbers(dict_road_base_1, dict_road_base_1['numbers_1'])
# Dict_2 = round_dict_numbers(dict_road_base_2, dict_road_base_2['numbers_2'])
# Dict_3 = round_dict_numbers(dict_road_base_3, dict_road_base_3['numbers_3'])
# Dict_4 = round_dict_numbers(dict_road_base_4, dict_road_base_4['numbers_4'])
# Dict = dict(Dict_1, **Dict_2, **Dict_3, **Dict_4)
#
# print(Dict)
# print("=======================")
# filename_box = ['cr8', 'result_chapter8']
# save_path = r'C:\Users\Administrator\PycharmProjects\Odoo_addons_NB\autocrword\models\chapter_8'
# read_path = os.path.join(save_path, '%s.docx') % filename_box[0]
# save_path = os.path.join(save_path, '%s.docx') % filename_box[1]
# tpl = DocxTemplate(read_path)
# tpl.render(Dict)
# tpl.save(save_path)
# print("==========finished=============")
