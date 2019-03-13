from RoundUp import round_dict
import math, os
from EarthStoneBalanceSheet import EarthStoneBalanceSheet
from docxtpl import DocxTemplate


class WasteSlagEngineeringSheet(EarthStoneBalanceSheet):
    def __init__(self):
        self.waste_slag_area, self.waste_slag_volume, self.waste_slag_grass_area, self.waste_slag_drainage_ditches, \
        self.waste_slag_gutter, self.waste_slag_M75_retaining_wall = 0, 0, 0, 0, 0, 0

    def extraction_data_waste_slag(self):
        self.waste_slag_area = math.floor(self.sum_EarthStoneBalance_spoil / 100000 + 1) * 10000
        self.waste_slag_volume = math.floor(self.sum_EarthStoneBalance_spoil / 100000 + 1) * 100000
        self.waste_slag_grass_area = self.waste_slag_area * 1.25
        self.waste_slag_drainage_ditches = math.floor(self.sum_EarthStoneBalance_spoil / 100000 + 1) * 500 * 0.75
        self.waste_slag_gutter = math.floor(self.sum_EarthStoneBalance_spoil / 100000 + 1) * 480 * 0.35
        self.waste_slag_M75_retaining_wall = math.floor(self.sum_EarthStoneBalance_spoil / 100000 + 1) * 4.75 * 80

    def generate_dict_waste_slag(self):
        dict_waste_slag = {
            '弃渣场_面积': self.waste_slag_area,
            '弃渣场_容量': self.waste_slag_volume,
            '弃渣场_喷播植草': self.waste_slag_grass_area,
            '弃渣场_截水沟': self.waste_slag_drainage_ditches,
            '弃渣场_排水沟': self.waste_slag_gutter,
            '弃渣场_挡土墙': self.waste_slag_M75_retaining_wall,
        }
        return dict_waste_slag


# project07 = WasteSlagEngineeringSheet()
# data1 = project07.extraction_data_wind_resource(basic_type='扩展基础', ultimate_load=70000, fortification_intensity=7)
# numbers_list = [15]
# data_cal1 = project07.excavation_cal_wind_resource(data1, 0.8, 0.2, numbers_list)
#
# data2 = project07.extraction_data_box_voltage(3)
# data_cal2 = project07.excavation_cal_box_voltage(data2, 0.8, 0.2, numbers_list)
#
# data3 = project07.extraction_data_booster_station('新建', 110, 100)
# data_cal = project07.excavation_cal_booster_station(data3, 0.8, 0.2, '陡坡低山')
#
# numbers_list = [5, 1.5, 10, 15]
# data_1, data_2, data_3, data_4 = project07.extraction_data_road_basement('陡坡低山')
# data_ca1, data_ca2, data_ca3, data_ca4 = project07.excavation_cal_road_basement(data_1, data_2, data_3, data_4, '陡坡低山',
#                                                                                 0.8, 0.2, numbers_list)
# line_data = [15000, 10000]
# project07.extraction_data_earth_stone_balance(line_data[0], line_data[1])
#
# project07.extraction_data_waste_slag()
#
# Dict = round_dict(project07.generate_dict_waste_slag())
# print(Dict)
# filename_box = ['cr8', 'result_chapter8']
# save_path = r'C:\Users\Administrator\PycharmProjects\Odoo_addons_NB\autocrword\models\chapter_8'
# read_path = os.path.join(save_path, '%s.docx') % filename_box[0]
# save_path = os.path.join(save_path, '%s.docx') % filename_box[1]
# tpl = DocxTemplate(read_path)
# tpl.render(Dict)
# tpl.save(save_path)
