from docxtpl import DocxTemplate
import os
from MainConstructionQuantitySummarySheet import *
from chapter_8 import RoundUp

def get_dict(np, dict_keys):
    """
    结合传入np数组和dict_keys关键字参数，创建字典。注意一一对应。
    :param np:  传入数组
    :param dict_keys: 关键字字典
    :return: 返回字典

    """
    dict = {}
    for i in range(0, len(dict_keys)):
        key_dict = dict_keys[i]
        print(key_dict,np[:, i])
        value_dict = np[:, i]
        dict[key_dict] = value_dict
    return dict


def get_dict_8(np, dict_keys):
    """
    结合传入np数组和dict_keys关键字参数，创建字典。注意一一对应。
    :param np:  传入数组
    :param dict_keys: 关键字字典
    :return: 返回字典

    """
    dict = {}
    for i in range(0, len(dict_keys)):
        key_dict = dict_keys[i]
        value_dict = np[i]
        dict[key_dict] = value_dict
    return dict

def generate_civil_docx(turbine_numbers=0, basic_type='', ultimate_load=0, fortification_intensity=0,
                        basic_earthwork_ratio=0, basic_stone_ratio=0, TurbineCapacity=0, road_earthwork_ratio=0,
                        road_stone_ratio=0, Status='', Grade=0, Capacity=0, TerrainType='', numbers_list_road=[],
                        overhead_line=0, direct_buried_cable=0, line_data=[], main_booster_station_num=0,
                        overhead_line_num=0, direct_buried_cable_num=0):
    # turbine_numbers = 15

    project10 = MainConstructionQuantitySummarySheet()
    # data1 = project10.extraction_data_wind_resource(basic_type='扩展基础', ultimate_load=70000, fortification_intensity=7)
    data1 = project10.extraction_data_wind_resource(basic_type=basic_type, ultimate_load=ultimate_load,
                                                    fortification_intensity=fortification_intensity)
    data_cal1 = project10.excavation_cal_wind_resource(data1, basic_earthwork_ratio, basic_stone_ratio, turbine_numbers)
    Dict1 = RoundUp.round_dict_numbers(project10.generate_dict_wind_resource(data_cal1, turbine_numbers), turbine_numbers,2)
    # ==============================================
    data2 = project10.extraction_data_box_voltage(TurbineCapacity)
    data_cal2 = project10.excavation_cal_box_voltage(data2, basic_earthwork_ratio, basic_stone_ratio, turbine_numbers)
    dict_box_voltage = project10.generate_dict_box_voltage(data_cal2, turbine_numbers)
    Dict2 = RoundUp.round_dict_numbers(dict_box_voltage, turbine_numbers,1)
    # ==============================================
    # data3 = project10.extraction_data_booster_station('新建', 110, 100)
    data3 = project10.extraction_data_booster_station(Status, Grade, Capacity)
    data_cal = project10.excavation_cal_booster_station(data3, road_earthwork_ratio, road_stone_ratio, TerrainType)
    Dict3 = RoundUp.round_dict(project10.generate_dict_booster_station(data_cal))
    # ==============================================
    # numbers_list_road = [5, 1.5, 10, 15]
    data_1, data_2, data_3, data_4 = project10.extraction_data_road_basement(TerrainType)
    data_ca1, data_ca2, data_ca3, data_ca4 = \
        project10.excavation_cal_road_basement(data_1, data_2, data_3, data_4, road_earthwork_ratio,
                                               road_stone_ratio, TerrainType, numbers_list_road)

    dict_road_base_1, dict_road_base_2, dict_road_base_3, dict_road_base_4 = \
        project10.generate_dict_road_basement(data_ca1, data_ca2, data_ca3, data_ca4, numbers_list_road)
    Dict_1 = RoundUp.round_dict_numbers(dict_road_base_1, dict_road_base_1['numbers_1'],2)
    Dict_2 = RoundUp.round_dict_numbers(dict_road_base_2, dict_road_base_2['numbers_2'],2)
    Dict_3 = RoundUp.round_dict_numbers(dict_road_base_3, dict_road_base_3['numbers_3'],2)
    Dict_4 = RoundUp.round_dict_numbers(dict_road_base_4, dict_road_base_4['numbers_4'],2)
    Dict4 = dict(Dict_1, **Dict_2, **Dict_3, **Dict_4)
    # ==============================================

    project10.extraction_data_construction_land_use_summary(TurbineCapacity, turbine_numbers)
    Dict5 = RoundUp.round_dict(project10.generate_dict_construction_land_use_summary())
    # ==============================================
    project10.extraction_data_permanent_land_area()
    Dict6 = RoundUp.round_dict(project10.generate_dict_permanent_land_area())
    # ==============================================
    # line_data = [15000, 10000]
    project10.extraction_data_earth_stone_balance(line_data[0], line_data[1])
    Dict7 = RoundUp.round_dict(project10.generate_dict_earth_stone_balance())
    # ==============================================
    project10.extraction_data_waste_slag()
    Dict8 = RoundUp.round_dict(project10.generate_dict_waste_slag())
    # ==============================================
    # overhead_line = 1500
    # direct_buried_cable = 3000
    project10.extraction_data_temporary_land_area(numbers_list_road, overhead_line, direct_buried_cable)
    Dict9 = RoundUp.round_dict(project10.generate_dict_temporary_land_area())
    # ==============================================
    # main_booster_station_num = 2
    # overhead_line_num = 20
    # direct_buried_cable_num = 2
    project10.extraction_data_main_construction_quantity_summary(main_booster_station_num, overhead_line_num,
                                                                 direct_buried_cable_num)
    Dict10 = RoundUp.round_dict(project10.generate_dict_main_construction_quantity_summary())
    # print(Dict)
    Dict = dict(Dict1, **Dict2, **Dict3, **Dict4, **Dict5, **Dict6, **Dict7, **Dict8, **Dict9, **Dict10)
    filename_box = ['cr8', 'result_chapter8']
    save_path = r'C:\Users\Administrator\PycharmProjects\Odoo_addons_NB2\autocrword\models\source\chapter_8'
    read_path = os.path.join(save_path, '%s.docx') % filename_box[0]
    save_path = os.path.join(save_path, '%s.docx') % filename_box[1]
    tpl = DocxTemplate(read_path)
    tpl.render(Dict)
    tpl.save(save_path)
