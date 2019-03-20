# from RoundUp import round_dict
# from docxtpl import DocxTemplate
# import os
from WindResourceDatabase import WindResourceDatabase
from BoxVoltageDatabase import BoxVoltageDatabase
from BoosterStationDatabase import BoosterStationDatabase
from RoadBasementDatabase import RoadBasementDatabase


class EarthStoneBalanceSheet(WindResourceDatabase, BoxVoltageDatabase, BoosterStationDatabase, RoadBasementDatabase):
    def __init__(self):
        super().__init__()
        # ===========basic parameters==============
        self.total_line_excavation, self.total_line_back_fill, self.total_line_spoil = 0, 0, 0
        # ===========Calculated parameters==============
        self.turbine_foundation_box_voltage_excavation, self.turbine_foundation_box_voltage_back_fill = 0, 0
        self.turbine_foundation_box_voltage_spoil = 0

        self.booster_station_engineering_excavation, self.booster_station_engineering_back_fill = 0, 0
        self.booster_station_engineering_spoil = 0

        self.road_engineering_excavation, self.road_engineering_back_fill, self.road_engineering_spoil = 0, 0, 0
        self.hoisting_platform_excavation, self.hoisting_platform_back_fill, self.hoisting_platform_spoil = 0, 0, 0
        self.sum_EarthStoneBalance_excavation, self.sum_EarthStoneBalance_back_fill = 0, 0
        self.sum_EarthStoneBalance_spoil = 0

    def extraction_data_earth_stone_balance(self, total_line_excavation, total_line_back_fill):
        # **********
        self.turbine_foundation_box_voltage_excavation = self.earth_excavation_wind_resource_numbers.iat[0] + \
                                                         self.stone_excavation_wind_resource_numbers.iat[0] + \
                                                         self.earth_excavation_box_voltage_numbers.iat[0] + \
                                                         self.stone_excavation_box_voltage_numbers.iat[0]

        self.turbine_foundation_box_voltage_back_fill = \
            self.earth_work_back_fill_wind_resource_numbers.iat[0] + self.earthwork_back_fill_box_voltage_numbers.iat[0]

        self.turbine_foundation_box_voltage_spoil = \
            self.turbine_foundation_box_voltage_excavation - self.turbine_foundation_box_voltage_back_fill

        # **********
        self.booster_station_engineering_excavation = \
            self.earth_excavation_booster_station.iat[0] + self.stone_excavation_booster_station.iat[0]
        self.booster_station_engineering_back_fill = self.earthwork_back_fill_booster_station.iat[0]
        self.booster_station_engineering_spoil = \
            self.booster_station_engineering_excavation - self.booster_station_engineering_back_fill

        # **********
        self.road_engineering_excavation = \
            self.earth_road_base_excavation_1_numbers + self.stone_road_base_excavation_1_numbers + \
            self.earth_road_base_excavation_2_numbers + self.stone_road_base_excavation_2_numbers + \
            self.earth_road_base_excavation_3_numbers + self.stone_road_base_excavation_3_numbers

        self.road_engineering_back_fill = \
            self.earthwork_road_base_back_fill_1_numbers + self.earthwork_road_base_back_fill_2_numbers + \
            self.earthwork_road_base_back_fill_3_numbers
        self.road_engineering_spoil = self.road_engineering_excavation - self.road_engineering_back_fill

        # **********
        self.hoisting_platform_excavation = \
            self.earth_road_base_excavation_4_numbers.iat[0] + self.stone_road_base_excavation_4_numbers.iat[0]
        self.hoisting_platform_back_fill = self.earthwork_road_base_back_fill_4_numbers.iat[0]
        self.hoisting_platform_spoil = self.hoisting_platform_excavation - self.hoisting_platform_back_fill

        # **********
        self.total_line_excavation = total_line_excavation
        self.total_line_back_fill = total_line_back_fill
        self.total_line_spoil = self.total_line_excavation - self.total_line_back_fill

        # **********
        self.sum_EarthStoneBalance_excavation = \
            self.turbine_foundation_box_voltage_excavation + self.booster_station_engineering_excavation + \
            self.road_engineering_excavation + self.hoisting_platform_excavation + self.total_line_excavation

        self.sum_EarthStoneBalance_back_fill = \
            self.turbine_foundation_box_voltage_back_fill + self.booster_station_engineering_back_fill + \
            self.road_engineering_back_fill + self.hoisting_platform_back_fill + self.total_line_back_fill

        self.sum_EarthStoneBalance_spoil = \
            self.turbine_foundation_box_voltage_spoil + self.booster_station_engineering_spoil + \
            self.road_engineering_spoil + self.hoisting_platform_spoil + self.total_line_spoil

    def generate_dict_earth_stone_balance(self):
        dict_earth_stone_balance = {
            '风机基础及箱变_开挖': self.turbine_foundation_box_voltage_excavation,
            '风机基础及箱变_回填': self.turbine_foundation_box_voltage_back_fill,
            '风机基础及箱变_弃土': self.turbine_foundation_box_voltage_spoil,
            '升压站工程_开挖': self.booster_station_engineering_excavation,
            '升压站工程_回填': self.booster_station_engineering_back_fill,
            '升压站工程_弃土': self.booster_station_engineering_spoil,
            '道路工程_开挖': self.road_engineering_excavation,
            '道路工程_回填': self.road_engineering_back_fill,
            '道路工程_弃土': self.road_engineering_spoil,
            '吊装平台_开挖': self.hoisting_platform_excavation,
            '吊装平台_回填': self.hoisting_platform_back_fill,
            '吊装平台_弃土': self.hoisting_platform_spoil,
            '集电线路_开挖': self.total_line_excavation,
            '集电线路_回填': self.total_line_back_fill,
            '集电线路_弃土': self.total_line_spoil,
            '合计_开挖': self.sum_EarthStoneBalance_excavation,
            '合计_回填': self.sum_EarthStoneBalance_back_fill,
            '合计_弃土': self.sum_EarthStoneBalance_spoil,
        }
        return dict_earth_stone_balance

#
# project06 = EarthStoneBalanceSheet()
# data1 = project06.extraction_data_wind_resource(basic_type='扩展基础', ultimate_load=70000, fortification_intensity=7)
# numbers_list = [15]
# data_cal1 = project06.excavation_cal_wind_resource(data1, 0.8, 0.2, numbers_list)
#
# data2 = project06.extraction_data_box_voltage(3)
# data_cal2 = project06.excavation_cal_box_voltage(data2, 0.8, 0.2, numbers_list)
#
# data3 = project06.extraction_data_booster_station('新建', 110, 100)
# data_cal = project06.excavation_cal_booster_station(data3, 0.8, 0.2, '陡坡低山')
#
# numbers_list = [5, 1.5, 10, 15]
# data_1, data_2, data_3, data_4 = project06.extraction_data_road_basement('陡坡低山')
# data_ca1, data_ca2, data_ca3, data_ca4 = \
#     project06.excavation_cal_road_basement(data_1, data_2, data_3, data_4, '陡坡低山', 0.8, 0.2, numbers_list)
#
# line_data = [15000, 10000]
# project06.extraction_data_earth_stone_balance(line_data[0], line_data[1])
#
# Dict = round_dict(project06.generate_dict_earth_stone_balance())
# print(Dict)
# filename_box = ['cr8', 'result_chapter8']
# save_path = r'C:\Users\Administrator\PycharmProjects\Odoo_addons_NB\autocrword\models\chapter_8'
# read_path = os.path.join(save_path, '%s.docx') % filename_box[0]
# save_path = os.path.join(save_path, '%s.docx') % filename_box[1]
# tpl = DocxTemplate(read_path)
# tpl.render(Dict)
# tpl.save(save_path)
