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
        print(Data.loc[6,['grade']])
        print(Data.at[6, 'grade'])
        self.data = Data.loc[Data['status'] == self.status].loc[Data['grade'] == self.grade].loc[
            Data['capacity'] == self.capacity]
        return self.data

    def excavation_cal(self, basic_earthwork_ratio, basic_stone_ratio, terrain_type):
        self.basic_earthwork_ratio = basic_earthwork_ratio
        self.basic_stone_ratio = basic_stone_ratio
        self.terrain_type = terrain_type

        if self.terrain_type == ['平原']:
            self.slope_area = (self.data['long'] + 5) * (self.data['width'] + 5)
            self.earth_excavation = self.data['slope_area'] * 0.3 * self.basic_earthwork_ratio / 10
            self.stone_excavation = self.data['slope_area'] * 0.3 * self.basic_stone_ratio / 10
            self.earthwork_backfill = self.data['slope_area'] * 2
        else:
            self.slope_area = (self.data['long'] + 10) * (self.data['width'] + 10)
            self.earth_excavation = self.data['slope_area'] * 3 * self.basic_earthwork_ratio
            self.earth_excavation = self.data['slope_area'] * 3 * self.basic_stone_ratio
            self.earthwork_backfill = self.data['slope_area'] * 0.5

        self.data['Earthexcavation'] = self.earth_excavation
        self.data['Stoneexcavation'] = self.stone_excavation
        self.data['Earthworkbackfill'] = self.earthwork_backfill
        self.data['slope_area'] = self.slope_area
        return self.data


project03 = BoosterStationDatabase()
data = project03.extraction_data('新建', 110, 50)
print(data.at[0,'grade'])
