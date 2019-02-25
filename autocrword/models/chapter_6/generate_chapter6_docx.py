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
args_list = [25.3, 23.6, 1.55, 3, 31, 5]
Dict_6 = {}
project01 = WireRod(*args_list)
project01.aluminium_cable_steel_reinforced("LGJ_240_30")
args_chapter6_01 = ['钢芯铝绞线']
args_chapter6_01_type = ['LGJ_240_30']
print("---------线材生成完毕--------")

insulator_list = ['FXBW4_35_70', 'U70BP_146D', 'FPQ_35_4T16', 'YH5WZ_51_134']
tower_type_list = ['单回耐张塔', '单回耐张塔', '单回耐张塔', '单回直线塔', '单回直线塔', '双回耐张塔', '双回耐张塔', '双回直线塔', '双回直线塔', '铁塔电缆支架']
tower_type_high_list = ['J2-24', 'J4-24', 'FS-18', 'Z2-30', 'ZK-42', 'SJ2-24', 'SJ4-24', 'SZ2-30', 'SZK-42', '角钢']
tower_weight_list = [6.8, 8.5, 7, 5.5, 8.5, 12.5, 17, 6.5, 10, 0.5, ]
tower_height_list = [32, 32, 27, 37, 49, 37, 37, 42, 54, 0]
tower_foot_distance_list = [5.5, 5.5, 6, 5, 6, 7, 8, 6, 8, 0]

project02 = ElectricalInsulator(*args_list)
project02.sum_cal(tower_type_list, tower_type_high_list, tower_weight_list, tower_height_list, tower_foot_distance_list)
project02.electrical_insulator_model(*insulator_list)

args_chapter6_02_type = insulator_list


print("---------绝缘子生成完毕--------")

for i in range(0, len(args_chapter6_01_type)):
    key_dict = args_chapter6_01_type[i]
    value_dict = str(project01.aluminium_cable_steel_reinforced_length_weight)
    Dict_6[key_dict] = value_dict

for i in range(0, len(args_chapter6_02_type)):
    key_dict = args_chapter6_02_type[i]
    value_dict = str(project01.aluminium_cable_steel_reinforced_length_weight)
    Dict_6[key_dict] = value_dict

#
path_images = r"C:\Users\Administrator\PycharmProjects\docx_project\files\results"
# dict_keys_chapter5 = ['型号ID', '机组类型', '功率', '叶片数', '风轮直径', '扫风面积', '轮毂高度',
#                       '功率调节', '切入风速', '切出风速', '额定风速', '发电机型式', '额定功率', '电压', '频率',
#                       '塔架型式', '塔筒重量', '主制动系统', '第二制动', '三秒最大值']
# context_keys_chapter5 = ['机组类型', '功率', '叶片数', '风轮直径', '扫风面积', '轮毂高度', '功率调节', '切入风速',
#                          '切出风速', '额定风速', '发电机型式', '额定功率', '电压', '主制动系统', '第二制动', '三秒最大值']
# #  chapter 8
# args_chapter8 = {'foundation_type': '预制桩承台基础', 'max_load': 100000}
# dict_keys_chapter8 = ['ID', '基础型式', '极限荷载', '设防烈度', '承载力', '土方比', '底板半径R', '棱台顶面半径R1', '台柱半径R2',
#                       '底板外缘高度H1', '底板棱台高度H2', '台柱高度H3', '桩直径', '根数', '长度', '总桩长', '面积m2', '体积m3',
#                       '垫层', '土方开挖', '石方开挖', '土石方回填', '复合地基换填', '复合地基桩']
# context_keys_chapter8 = ['土方开挖', '石方开挖', '土石方回填', '体积m3', '垫层', '钢筋', '基础防水', '沉降观测']
# numbers = 20  # 风机个数
# print("机型选型：" + str(args_chapter5))
# print("基础选择参数：" + str(args_chapter8))
# print("风机数量：" + str(numbers))
# print("---------step:1  载入载入完毕--------")
# #
#
#
# # **********************************************
# print("*" * 30)
# print("---------开始 chapter 8--------")
# Dict_8 = get_dict(foundation_np, dict_keys_chapter8)
# print(Dict_8)
# context_8 = write_context_numbers(Dict_8, *context_keys_chapter8, numbers=numbers)
# context_8['钢筋'] = float('%.02f' % (float(Dict_8['体积m3']) / 10))
# context_8['钢筋numbers'] = float('%.02f' % (float(Dict_8['体积m3']) / 10 * numbers))
# context_8['基础防水'] = 1
# context_8['基础防水numbers'] = 1 * numbers
# context_8['沉降观测'] = 4
# context_8['沉降观测numbers'] = 4 * numbers
#
tpl = DocxTemplate(r'C:\Users\Administrator\PycharmProjects\Odoo_addons_NB\autocrword\models\CR_chapter6_template.docx')
tpl.render(Dict_6)
print(Dict_6)
tpl.save(r'C:\Users\Administrator\PycharmProjects\Odoo_addons_NB\autocrword\models\result_chapter6_a.docx')
print("---------chapter 6 生成完毕--------")
