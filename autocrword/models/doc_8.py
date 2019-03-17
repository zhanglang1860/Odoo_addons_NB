from docxtpl import DocxTemplate
import os
from chapter_8.MainConstructionQuantitySummarySheet import *
from chapter_8.RoundUp import round_dict

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
data_ca1, data_ca2, data_ca3, data_ca4 = project10.excavation_cal_road_basement(data_1, data_2, data_3, data_4, 0.8,
                                                                                0.2, '陡坡低山', numbers_list_road)
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
# print(Dict)
filename_box = ['cr8', 'result_chapter8']
save_path = r'C:\Users\Administrator\PycharmProjects\Odoo_addons_NB\autocrword\models\chapter_8'
read_path = os.path.join(save_path, '%s.docx') % filename_box[0]
save_path = os.path.join(save_path, '%s.docx') % filename_box[1]
tpl = DocxTemplate(read_path)
tpl.render(Dict)
tpl.save(save_path)
