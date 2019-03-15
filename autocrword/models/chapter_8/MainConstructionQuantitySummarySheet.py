from RoundUp import round_dict
from docxtpl import DocxTemplate
import os, math
from TemporaryLandAreaSheet import TemporaryLandAreaSheet


class MainConstructionQuantitySummarySheet(TemporaryLandAreaSheet):
    def __init__(self):
        self.construction_area, self.main_booster_station_num, self.overhead_line_num, \
        self.direct_buried_cable_num, self.earthwork_excavation, self.earthwork_backfill, self.concrete, \
        self.reinforcement, self.stone_masonry = 0, 0, 0, 0, 0, 0, 0, 0, 0

    def extraction_data_main_construction_quantity_summary(self, main_booster_station_num, overhead_line_num,
                                                           direct_buried_cable_num):
        self.construction_area = \
            self.data_booster_station.at[self.data_booster_station.index[0], 'ComprehensiveBuilding'] + \
            self.data_booster_station.at[self.data_booster_station.index[0], 'EquipmentBuilding'] + \
            self.data_booster_station.at[self.data_booster_station.index[0], 'AffiliatedBuilding']

        self.main_booster_station_num = main_booster_station_num
        self.overhead_line_num = overhead_line_num
        self.direct_buried_cable_num = direct_buried_cable_num
        self.earthwork_excavation = self.sum_EarthStoneBalance_excavation / 10000
        self.earthwork_backfill = self.sum_EarthStoneBalance_backfill / 10000

        self.concrete = \
            (self.c40_wind_resource_numbers + self.c15_wind_resource_numbers + self.c80_wind_resource_numbers +
             self.c35_box_voltage_numbers + self.c15_box_voltage_numbers + self.c30_booster_station +
             self.c15_booster_station + self.c15_oil_pool_booster_station + self.c30_oil_pool_booster_station +
             self.c25_foundation_booster_station + self.c30_road_base_2_numbers * 0.2 +
             self.c30_road_base_3_numbers * 0.2) / 10000

        self.reinforcement = \
            self.reinforcement_wind_resource_numbers + self.reinforcement_box_voltage_numbers + \
            self.reinforcement_booster_station

        self.stone_masonry = \
            (self.StoneMasonryDrainageDitch_1_numbers + self.MortarStoneRetainingWall_1_numbers +
             self.StoneMasonryDrainageDitch_2_numbers + self.MortarStoneRetainingWall_2_numbers +
             self.StoneMasonryDrainageDitch_3_numbers + self.MortarStoneRetainingWall_3_numbers +
             self.StoneMasonryDrainageDitch_4_numbers + self.MortarStoneRetainingWall_4_numbers +
             self.waste_slag_drainage_ditches + self.waste_slag_gutter + self.waste_slag_M75_retaining_wall) / 10000

    def generate_dict_main_construction_quantity_summary(self):
        dict_main_construction_quantity_summary = {
            '风机机组_主要施工工程量': self.turbine_numbers,
            '建筑面积_主要施工工程量': self.construction_area,
            '主变压器_主要施工工程量': self.main_booster_station_num,
            '架空线路_主要施工工程量': self.overhead_line_num,
            '直埋电缆_主要施工工程量': self.direct_buried_cable_num,
            '土石方开挖_主要施工工程量': self.earthwork_excavation,
            '土石方回填_主要施工工程量': self.earthwork_backfill,
            '混凝土_主要施工工程量': self.concrete,
            '钢筋_主要施工工程量': self.reinforcement,
            '浆砌石_主要施工工程量': self.stone_masonry,
        }
        return dict_main_construction_quantity_summary


project10 = MainConstructionQuantitySummarySheet()
data1 = project10.extraction_data_wind_resource(basic_type='扩展基础', ultimate_load=70000, fortification_intensity=7)
turbine_numbers = 15
data_cal1 = project10.excavation_cal_wind_resource(data1, 0.8, 0.2, turbine_numbers)

data2 = project10.extraction_data_box_voltage(3)
data_cal2 = project10.excavation_cal_box_voltage(data2, 0.8, 0.2, turbine_numbers)

data3 = project10.extraction_data_booster_station('新建', 110, 100)
data_cal = project10.excavation_cal_booster_station(data3, 0.8, 0.2, '陡坡低山')

numbers_list_road = [5, 1.5, 10, 15]
data_1, data_2, data_3, data_4 = project10.extraction_data_road_basement('陡坡低山')
data_ca1, data_ca2, data_ca3, data_ca4 = project10.excavation_cal_road_basement(data_1, data_2, data_3, data_4, '陡坡低山',
                                                                                0.8, 0.2, numbers_list_road)
turbine_capacity = 3
overhead_line = 1500
direct_buried_cable = 3000
project10.extraction_data_construction_land_use_summary(turbine_capacity, turbine_numbers)
project10.extraction_data_permanent_land_area()
line_data = [15000, 10000]
project10.extraction_data_earth_stone_balance(line_data[0], line_data[1])
project10.extraction_data_waste_slag()
project10.extraction_data_temporary_land_area(numbers_list_road, overhead_line, direct_buried_cable)
main_booster_station_num = 2
overhead_line_num = 20
direct_buried_cable_num = 2
project10.extraction_data_main_construction_quantity_summary(main_booster_station_num, overhead_line_num,
                                                             direct_buried_cable_num)

Dict = round_dict(project10.generate_dict_main_construction_quantity_summary())
print(Dict)
filename_box = ['cr8', 'result_chapter8']
save_path = r'C:\Users\Administrator\PycharmProjects\Odoo_addons_NB\autocrword\models\chapter_8'
read_path = os.path.join(save_path, '%s.docx') % filename_box[0]
save_path = os.path.join(save_path, '%s.docx') % filename_box[1]
tpl = DocxTemplate(read_path)
tpl.render(Dict)
tpl.save(save_path)
