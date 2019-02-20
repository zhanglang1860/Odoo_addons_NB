# -*- coding: utf-8 -*-
import xlrd
import xlwt
from datetime import date, datetime
from docxtpl import *
from docxtpl import DocxTemplate, InlineImage
# for height and width you have to use millimeters (Mm), inches or points(Pt) class :
from docx.shared import Mm, Inches, Pt
import jinja2
from jinja2.utils import Markup

def read_excel():
    # 打开文件
    workbook = xlrd.open_workbook(r'C:\autoreport\风资源工作簿-zyc修改.xlsm')
    tpl = DocxTemplate(r'C:\autoreport\华润template.docx')
    images = r'C:\autoreport\12345.png'
    # 获取所有sheet
    print(workbook.sheet_names())
    sheet2_name = workbook.sheet_names()[1]

    # 根据sheet索引或者名称获取sheet内容
    # sheet2 = workbook.sheet_by_index(1)  # sheet索引从0开始
    sheet2 = workbook.sheet_by_name('风电场概况')
    number_of_tower=sheet2.cell(15, 5)
    # sheet的名称，行数，列数
    print(sheet2.name, sheet2.nrows, sheet2.ncols)

    context = {'number_of_tower': InlineImage(tpl,images,width=Mm(20))}
    tpl.render(context)
    tpl.save(r'C:\autoreport\result.docx')

    # 获取整行和整列的值（数组）
    # rows = sheet2.row_values(15)  # 获取第四行内容
    # cols = sheet2.col_values(3)  # 获取第三列内容
    # print(rows)
    # print(cols)

    # 获取单元格内容
    print(sheet2.cell(15, 5))
    # 获取单元格内容的数据类型
    print(sheet2.cell(15, 5).ctype)


# if __name__ == '__main__':
#     read_excel()