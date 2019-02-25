import os
# from generate_images import generate_images
from docxtpl import DocxTemplate, InlineImage

from generate_dict import get_dict, write_context_numbers, write_context

from ElectricalCircuit import ElectricalCircuit
from WireRod import WireRod
from ElectricalInsulator import ElectricalInsulator
from TowerType import TowerType
from RoundUp import round_up
from Cable import Cable

# **********************************************
print("*" * 30)
# step:1
# 载入参数
print("---------step:1  载入参数--------")
#  chapter 6
args_list = [19, 22, 8, 1.5, 40, 6]
Dict_6 = {}
project01 = WireRod(*args_list)
project01.aluminium_cable_steel_reinforced("LGJ_240_30")
args_chapter6_01 = ['钢芯铝绞线']
args_chapter6_01_type = ['LGJ_240_30']

for i in range(0, len(args_chapter6_01_type)):
    key_dict = args_chapter6_01_type[i]
    if key_dict == 'LGJ_240_30':
        value_dict = str(project01.aluminium_cable_steel_reinforced_length_weight)
        Dict_6[key_dict] = value_dict
print("---------线材生成完毕--------")

insulator_list = ['FXBW4_35_70', 'U70BP_146D', 'FPQ_35_4T16', 'YH5WZ_51_134']
tower_type_list = ['单回耐张塔', '单回耐张塔', '单回耐张塔', '单回直线塔', '单回直线塔', '双回耐张塔', '双回耐张塔', '双回直线塔', '双回直线塔', '铁塔电缆支架']
tower_type_high_list = ['J2-24', 'J4-24', 'FS-18', 'Z2-30', 'ZK-42', 'SJ2-24', 'SJ4-24', 'SZ2-30', 'SZK-42', '角钢']
tower_weight_list = [6.8, 8.5, 7, 5.5, 8.5, 12.5, 17, 6.5, 10, 0.5, ]
tower_height_list = [32, 32, 27, 37, 49, 37, 37, 42, 54, 0]
tower_foot_distance_list = [5.5, 5.5, 6, 5, 6, 7, 8, 6, 8, 0]

project02 = ElectricalInsulator(*args_list)
project02.sum_cal_tower_type(tower_type_list, tower_type_high_list, tower_weight_list, tower_height_list, tower_foot_distance_list)
project02.electrical_insulator_model(*insulator_list)

args_chapter6_02_type = insulator_list

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





#
path_images = r"C:\Users\Administrator\PycharmProjects\docx_project\files\results"
tpl = DocxTemplate(r'C:\Users\Administrator\PycharmProjects\Odoo_addons_NB\autocrword\models\CR_chapter6_template.docx')
tpl.render(Dict_6)
print(Dict_6)
tpl.save(r'C:\Users\Administrator\PycharmProjects\Odoo_addons_NB\autocrword\models\result_chapter6_b.docx')
print("---------chapter 6 生成完毕--------")
