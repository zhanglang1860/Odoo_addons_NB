# from RoundUp import round_dict
# from docxtpl import DocxTemplate
# import os
from WindResourceDatabase import WindResourceDatabase
from BoxVoltageDatabase import BoxVoltageDatabase
from BoosterStationDatabase import BoosterStationDatabase
from RoadBasementDatabase import RoadBasementDatabase


class PermanentLandAreaSheet(WindResourceDatabase, BoxVoltageDatabase, BoosterStationDatabase, RoadBasementDatabase):
    def __init__(self):
        self.wind_turbine_foundation, self.box_voltage_foundation, self.booster_station_foundation, \
        self.sum_foundation, self.sum_acres_foundation = 0, 0, 0, 0, 0

    def extraction_data_permanent_land_area(self):
        self.wind_turbine_foundation = self.data_wind_resource.at[self.data_wind_resource.index[0], 'Area']
        self.box_voltage_foundation = self.data_box_voltage.at[self.data_box_voltage.index[0], 'Area']
        self.booster_station_foundation = self.data_booster_station.at[self.data_booster_station.index[0], 'SlopeArea']
        self.sum_foundation = self.wind_turbine_foundation + self.box_voltage_foundation + self.booster_station_foundation
        self.sum_acres_foundation = self.sum_foundation / 666.667

    def generate_dict_permanent_land_area(self):
        dict_permanent_land_area = {
            '风电机组基础_永久用地面积': self.wind_turbine_foundation,
            '箱变基础_永久用地面积': self.box_voltage_foundation,
            '变电站_永久用地面积': self.booster_station_foundation,
            '合计_永久用地面积': self.sum_foundation,
            '合计亩_永久用地面积': self.sum_acres_foundation,
         }
        return dict_permanent_land_area

# project08 = PermanentLandAreaSheet()
# data1 = project08.extraction_data_wind_resource(basic_type='扩展基础', ultimate_load=70000, fortification_intensity=7)
# numbers_list = [15]
# data_cal1 = project08.excavation_cal_wind_resource(data1, 0.8, 0.2, numbers_list)
#
# data2 = project08.extraction_data_box_voltage(3)
# data_cal2 = project08.excavation_cal_box_voltage(data2, 0.8, 0.2, numbers_list)
#
# data3 = project08.extraction_data_booster_station('新建', 110, 100)
# data_cal = project08.excavation_cal_booster_station(data3, 0.8, 0.2, '陡坡低山')
#
# numbers_list = [5, 1.5, 10, 15]
# data_1, data_2, data_3, data_4 = project08.extraction_data_road_basement('陡坡低山')
# data_ca1, data_ca2, data_ca3, data_ca4 = project08.excavation_cal_road_basement(data_1, data_2, data_3, data_4, '陡坡低山',
#                                                                                 0.8, 0.2, numbers_list)
#
# project08.extraction_data_permanent_land_area()
#
# Dict = round_dict(project08.generate_dict_permanent_land_area())
# print(Dict)
# filename_box = ['cr8', 'result_chapter8']
# save_path = r'C:\Users\Administrator\PycharmProjects\Odoo_addons_NB\autocrword\models\chapter_8'
# read_path = os.path.join(save_path, '%s.docx') % filename_box[0]
# save_path = os.path.join(save_path, '%s.docx') % filename_box[1]
# tpl = DocxTemplate(read_path)
# tpl.render(Dict)
# tpl.save(save_path)