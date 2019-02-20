import os
# from generate_images import generate_images
from docxtpl import DocxTemplate, InlineImage
# from foundation_args_chapter8 import foundation_args_chapter8
from generate_dict import get_dict, write_context_numbers,write_context
from connect_sql import connect_sql_chapter5, connect_sql_chapter8
from addons.autocrword.models.wind_f import windenergy_specialty
# **********************************************
print("*" * 30)
# step:1
# 载入参数
print("---------step:1  载入参数--------")
args_chapter5=windenergy_specialty.generator_ids.Name
#  chapter 5
args_chapter5 = ['GW3.3-155', 'MY2.5-145', 'GW3.0-140', 'GW3.4-140', 'GW2.5-140']
path_images = r"C:\Users\Administrator\PycharmProjects\docx_project\files\results"
dict_keys_chapter5 = ['型号ID', '机组类型', '功率', '叶片数', '风轮直径', '扫风面积', '轮毂高度',
                      '功率调节', '切入风速', '切出风速', '额定风速', '发电机型式', '额定功率', '电压', '频率',
                      '塔架型式', '塔筒重量', '主制动系统', '第二制动', '三秒最大值']
context_keys_chapter5 = ['机组类型', '功率', '叶片数', '风轮直径', '扫风面积', '轮毂高度', '功率调节', '切入风速',
                         '切出风速', '额定风速', '发电机型式', '额定功率', '电压', '主制动系统', '第二制动','三秒最大值']
#  chapter 8
args_chapter8 = {'foundation_type': '预制桩承台基础', 'max_load': 100000}
dict_keys_chapter8 = ['ID', '基础型式', '极限荷载', '设防烈度', '承载力', '土方比', '底板半径R', '棱台顶面半径R1', '台柱半径R2',
                      '底板外缘高度H1', '底板棱台高度H2', '台柱高度H3', '桩直径', '根数', '长度', '总桩长', '面积m2', '体积m3',
                      '垫层', '土方开挖', '石方开挖', '土石方回填', '复合地基换填', '复合地基桩']
context_keys_chapter8 = ['土方开挖', '石方开挖', '土石方回填', '体积m3', '垫层', '钢筋', '基础防水', '沉降观测']
numbers = 20  # 风机个数
print("机型选型：" + str(args_chapter5))
print("基础选择参数：" + str(args_chapter8))
print("风机数量：" + str(numbers))
print("---------step:1  载入载入完毕--------")
#
# **********************************************
print("*" * 30)
# step:2
# 生成数组
print("---------step:2  生成数组--------")
tur_np, power_np, efficiency_np = connect_sql_chapter5(*args_chapter5)  # 一会儿注释connect_sql_chapter5
sql_foundation, key_vaule = foundation_args_chapter8(**args_chapter8)
foundation_np = connect_sql_chapter8(sql_foundation, *key_vaule)
print("机型选型数组：" + str(tur_np))
print("功率曲线数组：" + str(power_np))
print("机型效率数组：" + str(efficiency_np))
print("---------step:2  生成数组完毕--------")

# **********************************************
print("*" * 30)
# step:3
# 生成图片
print("---------step:3  生成图片--------")
generate_images(path_images, power_np, efficiency_np)  # 一会儿注释generate_images
print("---------step:3  生成图片完毕--------")

# **********************************************
print("*" * 30)
# step:4
# 生成报告
# **********************************************
print("*" * 30)
print("---------step:4  生成报告--------")
print("---------开始 chapter 5--------")
# chapter 5
tpl = DocxTemplate(r'C:\Users\Administrator\PycharmProjects\docx_project\files\CR_chapter5_template.docx')
context = {}
Dict_5 = get_dict(tur_np, dict_keys_chapter5)
context_5 = write_context(Dict_5, *context_keys_chapter5)
png_box = ('powers', 'efficiency')
for i in range(0, 2):
    key = 'myimage' + str(i)
    value = InlineImage(tpl, os.path.join(path_images, '%s.png') % png_box[i])
    context_5[key] = value
tpl.render(context_5)
tpl.save(r'C:\Users\Administrator\PycharmProjects\docx_project\files\results\result_chapter5-a.docx')
print("---------chapter 5 生成完毕--------")
# **********************************************
print("*" * 30)
print("---------开始 chapter 8--------")
Dict_8 = get_dict(foundation_np, dict_keys_chapter8)
print(Dict_8)
context_8 = write_context_numbers(Dict_8, *context_keys_chapter8, numbers=numbers)
context_8['钢筋'] = float('%.02f' % (float(Dict_8['体积m3']) / 10))
context_8['钢筋numbers'] = float('%.02f' % (float(Dict_8['体积m3']) / 10 * numbers))
context_8['基础防水'] = 1
context_8['基础防水numbers'] = 1 * numbers
context_8['沉降观测'] = 4
context_8['沉降观测numbers'] = 4 * numbers

tpl = DocxTemplate(r'C:\Users\Administrator\PycharmProjects\docx_project\files\CR_chapter8_template.docx')
tpl.render(context_8)
print(context_8)
tpl.save(r'C:\Users\Administrator\PycharmProjects\docx_project\files\results\result_chapter8_a.docx')
print("---------chapter 8 生成完毕--------")
