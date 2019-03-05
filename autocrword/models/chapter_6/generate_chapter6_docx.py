from docxtpl import DocxTemplate
from WireRod import WireRod
from ElectricalInsulator import ElectricalInsulator
from TowerType import TowerType
from TowerBase import TowerBase
from Cable import Cable

# **********************************************
print("*" * 30)
# step:1
# 载入参数
print("---------step:1  载入参数--------")
#  chapter 6
Dict_6 = {}
project_chapter6_type = ['山地']
args=[19, 22, 8, 1.5, 40, 6]
project01 = WireRod(project_chapter6_type, *args)
project01.aluminium_cable_steel_reinforced("LGJ_240_30")
args_chapter6_01_name = ['钢芯铝绞线']
args_chapter6_01_type = ['LGJ_240_30']

for i in range(0, len(args_chapter6_01_name)):
    if args_chapter6_01_name[i]=='钢芯铝绞线':
        print("---------线材:钢芯铝绞线--------")
        key_dict = args_chapter6_01_type[i]
        if key_dict == 'LGJ_240_30':
            value_dict = str(project01.aluminium_cable_steel_reinforced_length_weight)
            Dict_6[key_dict] = value_dict
print("---------线材生成完毕--------")

electrical_insulator_name_list = ['复合绝缘子', '瓷绝缘子', '复合针式绝缘子', '复合外套氧化锌避雷器']
electrical_insulator_type_list = ['FXBW4_35_70', 'U70BP_146D', 'FPQ_35_4T16', 'YH5WZ_51_134']

tower_type_list = ['单回耐张塔', '单回耐张塔', '单回耐张塔', '单回直线塔', '单回直线塔', '双回耐张塔', '双回耐张塔', '双回直线塔', '双回直线塔', '铁塔电缆支架']
tower_type_high_list = ['J2_24', 'J4_24', 'FS_18', 'Z2_30', 'ZK_42', 'SJ2_24', 'SJ4_24', 'SZ2_30', 'SZK_42', '角钢']
tower_weight_list = [6.8, 8.5, 7, 5.5, 8.5, 12.5, 17, 6.5, 10, 0.5, ]
tower_height_list = [32, 32, 27, 37, 49, 37, 37, 42, 54, 0]
tower_foot_distance_list = [5.5, 5.5, 6, 5, 6, 7, 8, 6, 8, 0]

project_chapter6_type = ['山地']
project02 = ElectricalInsulator(project_chapter6_type, *args)
project02.sum_cal_tower_type(tower_type_list, tower_type_high_list, tower_weight_list, tower_height_list,
                             tower_foot_distance_list)
project02.electrical_insulator_model(project_chapter6_type, electrical_insulator_name_list,
                                     electrical_insulator_type_list)

args_chapter6_02_type = electrical_insulator_type_list

for i in range(0, len(args_chapter6_02_type)):
    key_dict = args_chapter6_02_type[i]
    if key_dict == 'FXBW4_35_70':
        value_dict = str(project02.used_numbers_FXBW4_35_70)
        Dict_6[key_dict] = value_dict
    if key_dict == 'U70BP_146D':
        value_dict = str(project02.used_numbers_U70BP_146D)
        Dict_6[key_dict] = value_dict
    if key_dict == 'FPQ_35_4T16':
        value_dict = str(project02.used_numbers_FPQ_35_4T16)
        Dict_6[key_dict] = value_dict
    if key_dict == 'YH5WZ_51_134':
        value_dict = str(project02.used_numbers_YH5WZ_51_134)
        Dict_6[key_dict] = value_dict

print("---------绝缘子生成完毕--------")

args_chapter6_03_type = tower_type_high_list
project03 = TowerType(project_chapter6_type,*args)
project03.sum_cal_tower_type(tower_type_list, tower_type_high_list, tower_weight_list, tower_height_list,
                             tower_foot_distance_list)

for i in range(0, len(args_chapter6_03_type)):
    key_dict = args_chapter6_03_type[i]
    if key_dict == 'J2_24':
        value_dict = str(project03.used_numbers_single_J2_24)
        Dict_6[key_dict] = value_dict
    if key_dict == 'J4_24':
        value_dict = str(project03.used_numbers_single_J4_24)
        Dict_6[key_dict] = value_dict
    if key_dict == 'FS_18':
        value_dict = str(project03.used_numbers_single_FS_18)
        Dict_6[key_dict] = value_dict
    if key_dict == 'Z2_30':
        value_dict = str(project03.used_numbers_single_Z2_30)
        Dict_6[key_dict] = value_dict
    if key_dict == 'ZK_42':
        value_dict = str(project03.used_numbers_single_ZK_42)
        Dict_6[key_dict] = value_dict
    if key_dict == 'SJ2_24':
        value_dict = str(project03.used_numbers_double_SJ2_24)
        Dict_6[key_dict] = value_dict
    if key_dict == 'SJ4_24':
        value_dict = str(project03.used_numbers_double_SJ4_24)
        Dict_6[key_dict] = value_dict
    if key_dict == 'SZ2_30':
        value_dict = str(project03.used_numbers_double_SZ2_30)
        Dict_6[key_dict] = value_dict
    if key_dict == 'SZK_42':
        value_dict = str(project03.used_numbers_double_SZK_42)
        Dict_6[key_dict] = value_dict
    if key_dict == '角钢':
        value_dict = str(project03.used_numbers_angle_steel)
        Dict_6[key_dict] = value_dict

Dict_6['铁塔合计'] = str(project03.sum_used_numbers)

print("---------铁塔生成完毕--------")

tower_base_list = ['ZJC1', 'ZJC2', 'JJC1', 'JJC2', 'TW1', 'TW2', '基础垫层']
c25_unit_list = [12, 16, 42, 80, 8.8, 10.2, 2.4]
steel_unit_list = [300, 500, 750, 900, 600, 800, 0]
foot_bolt_list = [100, 180, 280, 360, 100, 180, 0]

args_chapter6_04_type = tower_base_list
project04 = TowerBase(project_chapter6_type,*args)
project04.sum_cal_tower_type(tower_type_list, tower_type_high_list, tower_weight_list, tower_height_list,
                             tower_foot_distance_list)
project04.sum_cal_tower_base(tower_base_list, c25_unit_list, steel_unit_list, foot_bolt_list)

for i in range(0, len(args_chapter6_04_type)):
    key_dict = args_chapter6_04_type[i]
    if key_dict == 'ZJC1':
        Dict_6['ZJC1_num'] = str(project04.used_numbers_base_zjc1)
        Dict_6['c25_sum_zjc1'] = str(project04.c25_sum_zjc1)
        Dict_6['steel_sum_zjc1'] = str(project04.steel_sum_zjc1)

    if key_dict == 'ZJC2':
        Dict_6['ZJC2_num'] = str(project04.used_numbers_base_zjc2)
        Dict_6['c25_sum_zjc2'] = str(project04.c25_sum_zjc2)
        Dict_6['steel_sum_zjc2'] = str(project04.steel_sum_zjc2)

    if key_dict == 'JJC1':
        Dict_6['JJC1_num'] = str(project04.used_numbers_base_jjc1)
        Dict_6['c25_sum_jjc1'] = str(project04.c25_sum_jjc1)
        Dict_6['steel_sum_jjc1'] = str(project04.steel_sum_jjc1)

    if key_dict == 'JJC2':
        Dict_6['jjc2_num'] = str(project04.used_numbers_base_jjc2)
        Dict_6['c25_sum_jjc2'] = str(project04.c25_sum_jjc2)
        Dict_6['steel_sum_jjc2'] = str(project04.steel_sum_jjc2)

    if key_dict == 'TW1':
        Dict_6['tw1_num'] = str(project04.used_numbers_base_tw1)
        Dict_6['c25_sum_tw1'] = str(project04.c25_sum_tw1)
        Dict_6['steel_sum_tw1'] = str(project04.steel_sum_tw1)
    if key_dict == 'TW2':
        Dict_6['tw2_num'] = str(project04.used_numbers_base_tw2)
        Dict_6['c25_sum_tw2'] = str(project04.c25_sum_tw2)
        Dict_6['steel_sum_tw2'] = str(project04.steel_sum_tw2)

    if key_dict == '基础垫层':
        Dict_6['base_layer'] = str(project04.used_numbers_base_layer)
        Dict_6['c25_sum_layer'] = str(project04.c25_sum_layer)
        Dict_6['steel_sum_layer'] = str(project04.steel_sum_layer)

Dict_6['基础数量合计'] = str(project04.used_numbers_base_sum)
Dict_6['基础混凝土合计'] = str(project04.c25_sum)
Dict_6['基础钢筋合计'] = str(project04.steel_sum)

print("---------铁塔基础生成完毕--------")

cable_project_list = ['高压电缆', '高压电缆', '电缆沟', '电缆终端', '电缆终端']
cable_model_list = ['YJLV22_26_35_3_95_gaoya', 'YJV22_26_35_1_300_gaoya', '电缆沟长度', 'YJLV22_26_35_3_95_dianlanzhongduan',
                    'YJV22_26_35_1_300_dianlanzhongduan']

args_chapter6_05_type = cable_model_list
project05 = Cable(project_chapter6_type,*args)
project05.sum_cal_cable(cable_project_list, cable_model_list)

for i in range(0, len(args_chapter6_05_type)):
    key_dict = args_chapter6_05_type[i]
    if key_dict == 'YJLV22_26_35_3_95_gaoya':
        Dict_6['YJLV22_26_35_3_95_gaoya'] = str(project05.cable_model_YJLV22_26_35_3_95_gaoya)
    if key_dict == 'YJV22_26_35_1_300_gaoya':
        Dict_6['YJV22_26_35_1_300_gaoya'] = str(project05.cable_model_YJV22_26_35_1_300_gaoya)
    if key_dict == '电缆沟长度':
        Dict_6['电缆沟长度'] = str(project05.cable_model_cable_duct)
    if key_dict == 'YJLV22_26_35_3_95_dianlanzhongduan':
        Dict_6['YJLV22_26_35_3_95_dianlanzhongduan'] = str(project05.cable_model_YJLV22_26_35_3_95_dianlanzhongduan)
    if key_dict == 'YJV22_26_35_1_300_dianlanzhongduan':
        Dict_6['YJV22_26_35_1_300_dianlanzhongduan'] = str(project05.cable_model_YJV22_26_35_1_300_dianlanzhongduan)
# print(Dict_6)
path_images = r"C:\Users\Administrator\PycharmProjects\docx_project\files\results"
tpl = DocxTemplate(r'C:\Users\Administrator\PycharmProjects\Odoo_addons_NB\autocrword\models\chapter_6\CR_chapter6_template.docx')
tpl.render(Dict_6)

tpl.save(r'C:\Users\Administrator\PycharmProjects\Odoo_addons_NB\autocrword\models\chapter_6\result_chapter6_d.docx')
print("---------chapter 6 生成完毕--------")
