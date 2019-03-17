from docxtpl import DocxTemplate
import os
from chapter_8.MainConstructionQuantitySummarySheet import *
from chapter_8.RoundUp import round_dict, round_dict_numbers

turbine_numbers = 15

project10 = MainConstructionQuantitySummarySheet()
data1 = project10.extraction_data_wind_resource(basic_type='扩展基础', ultimate_load=70000, fortification_intensity=7)
data_cal1 = project10.excavation_cal_wind_resource(data1, 0.8, 0.2, turbine_numbers)
Dict1 = round_dict_numbers(project10.generate_dict_wind_resource(data_cal1, turbine_numbers), turbine_numbers)
#==============================================
data2 = project10.extraction_data_box_voltage(3)
data_cal2 = project10.excavation_cal_box_voltage(data2, 0.8, 0.2, turbine_numbers)
dict_box_voltage = project10.generate_dict_box_voltage(data_cal2, turbine_numbers)
Dict2 = round_dict_numbers(dict_box_voltage, turbine_numbers)
#==============================================
data3 = project10.extraction_data_booster_station('新建', 110, 100)
data_cal = project10.excavation_cal_booster_station(data3, 0.8, 0.2, '陡坡低山')
Dict3 = round_dict(project10.generate_dict_booster_station(data_cal))
#==============================================
numbers_list_road = [5, 1.5, 10, 15]
data_1, data_2, data_3, data_4 = project10.extraction_data_road_basement('陡坡低山')
data_ca1, data_ca2, data_ca3, data_ca4 = project10.excavation_cal_road_basement(data_1, data_2, data_3, data_4, 0.8,
                                                                                0.2, '陡坡低山', numbers_list_road)

dict_road_base_1, dict_road_base_2, dict_road_base_3, dict_road_base_4 = \
    project10.generate_dict_road_basement(data_ca1, data_ca2, data_ca3, data_ca4, numbers_list_road)
Dict_1 = round_dict_numbers(dict_road_base_1, dict_road_base_1['numbers_1'])
Dict_2 = round_dict_numbers(dict_road_base_2, dict_road_base_2['numbers_2'])
Dict_3 = round_dict_numbers(dict_road_base_3, dict_road_base_3['numbers_3'])
Dict_4 = round_dict_numbers(dict_road_base_4, dict_road_base_4['numbers_4'])
Dict4 = dict(Dict_1, **Dict_2, **Dict_3, **Dict_4)
#==============================================
turbine_capacity = 3
overhead_line = 1500
direct_buried_cable = 3000
project10.extraction_data_construction_land_use_summary(turbine_capacity, turbine_numbers)
Dict5 = round_dict(project10.generate_dict_construction_land_use_summary())
#==============================================
project10.extraction_data_permanent_land_area()
Dict6 = round_dict(project10.generate_dict_permanent_land_area())
#==============================================
line_data = [15000, 10000]
project10.extraction_data_earth_stone_balance(line_data[0], line_data[1])
Dict7 = round_dict(project10.generate_dict_earth_stone_balance())
#==============================================
project10.extraction_data_waste_slag()
Dict8 = round_dict(project10.generate_dict_waste_slag())
#==============================================
project10.extraction_data_temporary_land_area(numbers_list_road, overhead_line, direct_buried_cable)
Dict9 = round_dict(project10.generate_dict_temporary_land_area())
#==============================================
main_booster_station_num = 2
overhead_line_num = 20
direct_buried_cable_num = 2
project10.extraction_data_main_construction_quantity_summary(main_booster_station_num, overhead_line_num,
                                                             direct_buried_cable_num)
Dict10 = round_dict(project10.generate_dict_main_construction_quantity_summary())
# print(Dict)
Dict = dict(Dict1, **Dict2, **Dict3, **Dict4, **Dict5, **Dict6, **Dict7, **Dict8, **Dict9, **Dict10)
filename_box = ['cr8', 'result_chapter8']
save_path = r'C:\Users\Administrator\PycharmProjects\Odoo_addons_NB\autocrword\models\chapter_8'
read_path = os.path.join(save_path, '%s.docx') % filename_box[0]
save_path = os.path.join(save_path, '%s.docx') % filename_box[1]
tpl = DocxTemplate(read_path)
tpl.render(Dict)
tpl.save(save_path)
