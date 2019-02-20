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
    print('hello fucking world')
    return True


# if __name__ == '__main__':
#     read_excel()