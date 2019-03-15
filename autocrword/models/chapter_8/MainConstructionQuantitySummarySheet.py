from RoundUp import round_dict
from docxtpl import DocxTemplate
import os, math
from BoosterStationDatabase import BoosterStationDatabase
from EarthStoneBalanceSheet import EarthStoneBalanceSheet
from PermanentLandAreaSheet import PermanentLandAreaSheet
from WasteSlagEngineeringSheet import WasteSlagEngineeringSheet


class MainConstructionQuantitySummarySheet(BoosterStationDatabase, EarthStoneBalanceSheet):
    def __init__(self):
        self.construction_area, self.main_booster_station_num, self.overhead_line_num, \
        self.direct_buried_cable_num, self.earthwork_excavation, self.approach_road, self.overhead_line_land, \
        self.direct_buried_cable_land, self.sum_temporary_land_area = 0, 0, 0, 0, 0, 0, 0, 0, 0

    def extraction_data_temporary_land_area(self, main_booster_station_num, overhead_line_num, direct_buried_cable_num):
        self.construction_area=self.data_booster_station.at[self.data_booster_station.index[0], 'ComprehensiveBuilding']\
                               +self.data_booster_station.at[self.data_booster_station.index[0], 'EquipmentBuilding']\
                               +self.data_booster_station.at[self.data_booster_station.index[0], 'AffiliatedBuilding']
        self.main_booster_station_num=main_booster_station_num
        self.overhead_line_num = overhead_line_num
        self.direct_buried_cable_num=direct_buried_cable_num
        self.earthwork_excavation=self.sum_EarthStoneBalance_excavation/10000
        self.earthwork_backfill = self.sum_EarthStoneBalance_backfill / 10000

        self.concrete=self.c40_wind_resource_numbers+self.c15_wind_resource_numbers+self.c80_wind_resource_numbers+\
                      self.c35_box_voltage_numbers+self.c15_box_voltage_numbers



    def generate_dict_temporary_land_area(self):
        dict_temporary_land_area = {
            '施工辅企_临时用地面积': self.construction_auxiliary_enterprise,
            '风电机组安装平台_临时用地面积': self.wind_turbine_installation_platform,
            '施工道路_临时用地面积': self.construction_road,
            '弃渣场_临时用地面积': self.waste_slag_yard,
            '进场道路_临时用地面积': self.approach_road,
            '架空线路_临时用地面积': self.overhead_line_land,
            '电缆沟_临时用地面积': self.direct_buried_cable_land,
            '合计_临时用地面积': self.sum_temporary_land_area,
            '合计亩_临时用地面积': self.sum_acres_temporary_land_area,
        }
        return dict_temporary_land_area


project09 = TemporaryLandAreaSheet()
data1 = project09.extraction_data_wind_resource(basic_type='扩展基础', ultimate_load=70000, fortification_intensity=7)
turbine_numbers = 15
data_cal1 = project09.excavation_cal_wind_resource(data1, 0.8, 0.2, turbine_numbers)

data2 = project09.extraction_data_box_voltage(3)
data_cal2 = project09.excavation_cal_box_voltage(data2, 0.8, 0.2, turbine_numbers)

data3 = project09.extraction_data_booster_station('新建', 110, 100)
data_cal = project09.excavation_cal_booster_station(data3, 0.8, 0.2, '陡坡低山')

numbers_list_road = [5, 1.5, 10, 15]
data_1, data_2, data_3, data_4 = project09.extraction_data_road_basement('陡坡低山')
data_ca1, data_ca2, data_ca3, data_ca4 = project09.excavation_cal_road_basement(data_1, data_2, data_3, data_4, '陡坡低山',
                                                                                0.8, 0.2, numbers_list_road)
turbine_capacity = 3
overhead_line = 1500
direct_buried_cable = 3000
project09.extraction_data_construction_land_use_summary(turbine_capacity, turbine_numbers)
project09.extraction_data_permanent_land_area()
line_data = [15000, 10000]
project09.extraction_data_earth_stone_balance(line_data[0], line_data[1])
project09.extraction_data_waste_slag()
project09.extraction_data_temporary_land_area(numbers_list_road, overhead_line, direct_buried_cable)

Dict = round_dict(project09.generate_dict_temporary_land_area())
print(Dict)
filename_box = ['cr8', 'result_chapter8']
save_path = r'C:\Users\Administrator\PycharmProjects\Odoo_addons_NB\autocrword\models\chapter_8'
read_path = os.path.join(save_path, '%s.docx') % filename_box[0]
save_path = os.path.join(save_path, '%s.docx') % filename_box[1]
tpl = DocxTemplate(read_path)
tpl.render(Dict)
tpl.save(save_path)
