import os
# from generate_images import generate_images
from docxtpl import DocxTemplate, InlineImage
from generate_dict import get_dict, write_context_numbers, write_context

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
