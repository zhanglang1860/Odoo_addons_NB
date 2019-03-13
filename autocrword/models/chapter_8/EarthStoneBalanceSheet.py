import pandas as pd
import numpy as np
from RoundUp import round_up, round_dict
from docxtpl import DocxTemplate
import math, os
from WindResourceDatabase import WindResourceDatabase
from BoxVoltageDatabase import BoxVoltageDatabase


class EarthStoneBalanceSheet(WindResourceDatabase, BoxVoltageDatabase):
    def __init__(self):
        self.turbine_foundation_box_voltage = 0

    # self.capacity, self.turbine_numbers = 0, 0
    # self.material_warehouse_1, self.temporary_residential_office_1, self.steel_processing_plant_1, \
    # self.equipment_storage_1, self.construction_machinery_parking_1, self.total_1 = 0, 0, 0, 0, 0, 0
    #
    # self.material_warehouse_2, self.temporary_residential_office_2, self.steel_processing_plant_2, \
    # self.equipment_storage_2, self.construction_machinery_parking_2, self.total_2 = 0, 0, 0, 0, 0, 0
    #
    # self.data = pd.DataFrame()

    def extraction_data_earth_stone_balance(self):
        # self.capacity = capacity
        self.turbine_foundation_box_voltage_excavation = \
            self.data_wind_resource.at[self.data_wind_resource.index[0], 'EarthExcavation_Turbine_Numbers'] + \
            self.data_wind_resource.at[self.data_wind_resource.index[0], 'StoneExcavation_Turbine_Numbers'] + \
            self.data_box_voltage.at[self.data_box_voltage.index[0], 'EarthExcavation_BoxVoltage_Numbers'] + \
            self.data_box_voltage.at[self.data_box_voltage.index[0], 'StoneExcavation_BoxVoltage_Numbers']

        self.turbine_foundation_box_voltage_backfill = \
            self.data_wind_resource.at[self.data_wind_resource.index[0], 'EarthWorkBackFill_Turbine_Numbers'] + \
            self.data_box_voltage.at[self.data_box_voltage.index[0], 'EarthWorkBackFill_BoxVoltage_Numbers']

        self.turbine_foundation_box_voltage_spoil = \
            self.turbine_foundation_box_voltage_Excavation - self.turbine_foundation_box_voltage_Backfill



    # def generate_dict(self):
    #     dict_construction_land_use_summary = {
    #         '材料仓库_1': self.material_warehouse_1,
    #         '材料仓库_2': self.material_warehouse_2,
    #         '临时住宅及办公室施工生活区_1': self.temporary_residential_office_1,
    #         '临时住宅及办公室施工生活区_2': self.temporary_residential_office_2,
    #         '钢筋加工厂_1': self.steel_processing_plant_1,
    #         '钢筋加工厂_2': self.steel_processing_plant_2,
    #         '设备存放场_1': self.equipment_storage_1,
    #         '设备存放场_2': self.equipment_storage_2,
    #         '施工机械停放场_1': self.construction_machinery_parking_1,
    #         '施工机械停放场_2': self.construction_machinery_parking_2,
    #         '合计_1': self.total_1,
    #         '合计_2': self.total_2,
    #     }
    #     return dict_construction_land_use_summary
    #


project06 = EarthStoneBalanceSheet()
data1 = project06.extraction_data_turbine(basic_type='扩展基础', ultimate_load=70000, fortification_intensity=7)
numbers_list = [15]
data_cal1 = project06.excavation_cal_turbine(0.8, 0.2, numbers_list)

data2 = project06.extraction_data_box_voltage(3)
data_cal2 = project06.excavation_cal_box_voltage(0.8, 0.2, numbers_list)
project06.extraction_data_earth_stone_balance()

print(project06.turbine_foundation_box_voltage_excavation, project06.turbine_foundation_box_voltage_backfill,
      project06.turbine_foundation_box_voltage_spoil)
#
# project05.extraction_data(3, 15)
# Dict = round_dict(project05.generate_dict())
# print(Dict)
# filename_box = ['cr8', 'result_chapter8']
# save_path = r'C:\Users\Administrator\PycharmProjects\Odoo_addons_NB\autocrword\models\chapter_8'
# read_path = os.path.join(save_path, '%s.docx') % filename_box[0]
# save_path = os.path.join(save_path, '%s.docx') % filename_box[1]
# tpl = DocxTemplate(read_path)
# tpl.render(Dict)
# tpl.save(save_path)
