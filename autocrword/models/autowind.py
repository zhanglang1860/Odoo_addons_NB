# -*- coding: utf-8 -*-

from odoo import models, fields, api
from . import renew2
import base64,os
from . import connect_sql
from . import generate_dict
# from . import generate_images
from docxtpl import DocxTemplate,InlineImage


class windenergy_specialty(models.Model):
    _name = 'autoreport.windenergy'
    _description = 'Wind energy input'
    _rec_name = 'project_id'
    project_id = fields.Many2one('autoreport.project', string=u'项目名', required=True)
    version_id = fields.Char(u'版本', required=True, default="1.0")
    installed_number = fields.Integer(u'机位数', required=True)
    generator_ids = fields.Many2many('autoreport.generator', required=True, string=u'比选机型')
    report_attachment_id = fields.Many2one('ir.attachment', string=u'可研报告风能章节')

    @api.multi
    def button_wind(self):
        projectname = self.project_id
        windattachmentid = projectname.wind_attachment_id
        myself = self
        projectname.wind_attachment_id = myself
        projectname.wind_attachment_ok = u"已提交,版本：" + self.version_id
        return True

    @api.multi
    def wind_generate(self):
        b = self.generator_ids
        print('tur:', b[1])
        print('old attachment：', self.report_attachment_id)
        if (str(self.report_attachment_id) != 'ir.attachment()'):
            print('old datas len：', len(self.report_attachment_id.datas))

        # renew2.read_excel()

        tur_name = []
        # tur_na = self.generator_ids
        for i in range(0, len(self.generator_ids)):
            tur_name.append(self.generator_ids[i].name_tur)

        data_tur_np, data_power_np, data_efficiency_np = connect_sql.connect_sql_chapter5(*tur_name)
        print(data_efficiency_np)
        #####################
        path_images = r"d:\Program Files (x86)\Odoo 12.0\server\addons\autocrword\models"
        print("---------step:3  生成图片--------")
        # generate_images.generate_images(path_images, data_power_np, data_efficiency_np)  # 一会儿注释generate_images
        print("---------step:3  生成图片完毕--------")

        #####################
        #  chapter 5

        dict_keys_chapter5 = ['型号ID', '功率', '叶片数', '风轮直径', '扫风面积', '轮毂高度',
                              '功率调节', '切入风速', '切出风速', '额定风速', '发电机型式', '额定功率', '电压', '频率',
                              '塔架型式', '塔筒重量', '主制动系统', '第二制动', '三秒最大值', 'datetime1id', 'datetime1',
                              'datetime2id', 'datetime2', '机组类型']
        context_keys_chapter5 = ['机组类型', '功率', '叶片数', '风轮直径', '扫风面积', '轮毂高度', '功率调节', '切入风速',
                                 '切出风速', '额定风速', '发电机型式', '额定功率', '电压', '主制动系统', '第二制动', '三秒最大值']

        print("---------开始 chapter 5--------")
        # chapter 5
        tpl = DocxTemplate(
            r'C:\Program Files (x86)\Odoo 12.0\server\addons\autocrword\models\CR_chapter5_template.docx')
        Dict_5 = generate_dict.get_dict(data_tur_np, dict_keys_chapter5)
        context_5 = generate_dict.write_context(Dict_5, *context_keys_chapter5)
        png_box = ('powers', 'efficiency')
        for i in range(0, 2):
            key = 'myimage' + str(i)
            value = InlineImage(tpl, os.path.join(path_images, '%s.png') % png_box[i])
            context_5[key] = value
        tpl.render(context_5)
        tpl.save(r'C:\Program Files (x86)\Odoo 12.0\server\addons\autocrword\models\result_chapter5_d.docx')
        print("---------chapter 5 生成完毕--------")

        ###########################

        reportfile_name = open(
            file=r'C:\Program Files (x86)\Odoo 12.0\server\addons\autocrword\models\result_chapter5_d.docx', mode='rb')
        byte = reportfile_name.read()
        reportfile_name.close()
        print('file lenth=', len(byte))
        base64.standard_b64encode(byte)
        if (str(self.report_attachment_id) == 'ir.attachment()'):
            Attachments = self.env['ir.attachment']
            print('开始创建新纪录')
            New = Attachments.create({
                'name': self.project_id.project_name + '可研报告风电章节下载页',
                'datas_fname': self.project_id.project_name + '可研报告风电章节.docx',
                'datas': base64.standard_b64encode(byte),
                'display_name': self.project_id.project_name + '可研报告风电章节',
                'create_date': fields.date.today(),
                'public': True,  # 此处需设置为true 否则attachments.read  读不到
                # 'mimetype': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
                # 'res_model': 'autoreport.project'
                # 'res_field': 'report_attachment_id'
            })
            print('已创建新纪录：', New)
            print('new dataslen：', len(New.datas))
            self.report_attachment_id = New
        else:
            self.report_attachment_id.datas = base64.standard_b64encode(byte)

        print('new attachment：', self.report_attachment_id)
        print('new datas len：', len(self.report_attachment_id.datas))
        return True


class outputcurve(models.Model):
    _name = 'autoreport.outputcurve'
    _description = 'Generator outputcurve'
    _rec_name = 'name_output'
    name_output = fields.Char(u'风机型号', required=True)
    speed2p5 = fields.Float(u'2.5m/s（kW）', required=True)
    speed3 = fields.Float(u'3m/s（kW）', required=True)
    speed4 = fields.Float(u'4m/s（kW）', required=True)
    speed5 = fields.Float(u'5m/s（kW）', required=True)
    speed6 = fields.Float(u'6m/s（kW）', required=True)
    speed7 = fields.Float(u'7m/s（kW）', required=True)
    speed8 = fields.Float(u'8m/s（kW）', required=True)
    speed9 = fields.Float(u'9m/s（kW）', required=True)
    speed10 = fields.Float(u'10m/s（kW）', required=True)
    speed11 = fields.Float(u'11m/s（kW）', required=True)
    speed12 = fields.Float(u'12m/s（kW）', required=True)
    speed13 = fields.Float(u'13m/s（kW）', required=True)
    speed14 = fields.Float(u'14m/s（kW）', required=True)
    speed15 = fields.Float(u'15m/s（kW）', required=True)
    speed16 = fields.Float(u'16m/s（kW）', required=True)
    speed17 = fields.Float(u'17m/s（kW）', required=True)
    speed18 = fields.Float(u'18m/s（kW）', required=True)
    speed19 = fields.Float(u'19m/s（kW）', required=True)
    speed20 = fields.Float(u'20m/s（kW）', required=True)
    speed21 = fields.Float(u'21m/s（kW）', required=True)
    speed22 = fields.Float(u'22m/s（kW）', required=True)
    speed23 = fields.Float(u'23m/s（kW）', required=True)
    speed24 = fields.Float(u'24m/s（kW）', required=True)
    speed25 = fields.Float(u'25m/s（kW）', required=True)


class outputcurve(models.Model):
    _name = 'autoreport.efficiency'
    _description = 'Generator efficiency'
    _rec_name = 'name_efficiency'
    name_efficiency = fields.Char(u'风机型号', required=True)
    speed2p5 = fields.Float(u'2.5m/s（kW）', required=True)
    speed3 = fields.Float(u'3m/s（kW）', required=True)
    speed4 = fields.Float(u'4m/s（kW）', required=True)
    speed5 = fields.Float(u'5m/s（kW）', required=True)
    speed6 = fields.Float(u'6m/s（kW）', required=True)
    speed7 = fields.Float(u'7m/s（kW）', required=True)
    speed8 = fields.Float(u'8m/s（kW）', required=True)
    speed9 = fields.Float(u'9m/s（kW）', required=True)
    speed10 = fields.Float(u'10m/s（kW）', required=True)
    speed11 = fields.Float(u'11m/s（kW）', required=True)
    speed12 = fields.Float(u'12m/s（kW）', required=True)
    speed13 = fields.Float(u'13m/s（kW）', required=True)
    speed14 = fields.Float(u'14m/s（kW）', required=True)
    speed15 = fields.Float(u'15m/s（kW）', required=True)
    speed16 = fields.Float(u'16m/s（kW）', required=True)
    speed17 = fields.Float(u'17m/s（kW）', required=True)
    speed18 = fields.Float(u'18m/s（kW）', required=True)
    speed19 = fields.Float(u'19m/s（kW）', required=True)
    speed20 = fields.Float(u'20m/s（kW）', required=True)
    speed21 = fields.Float(u'21m/s（kW）', required=True)
    speed22 = fields.Float(u'22m/s（kW）', required=True)
    speed23 = fields.Float(u'23m/s（kW）', required=True)
    speed24 = fields.Float(u'24m/s（kW）', required=True)
    speed25 = fields.Float(u'25m/s（kW）', required=True)


class generator(models.Model):
    _name = 'autoreport.generator'
    _description = 'Generator'
    _rec_name = 'name_tur'
    name_tur = fields.Char(u'风机型号', required=True)
    capacity = fields.Float(u'额定功率(kW)', required=True)
    blade_number = fields.Integer(u'叶片数', required=True)
    rotor_diameter = fields.Float(u'叶轮直径', required=True)
    rotor_swept_area = fields.Float(u'扫风面积', required=True)
    hub_height = fields.Char(u'轮毂高度')
    power_regulation = fields.Char(u'风机类型', required=True)
    cut_in_wind_speed = fields.Float(u'切入风速', required=True)
    cut_out_wind_speed = fields.Float(u'切出风速', required=True)
    rated_wind_speed = fields.Float(u'额定风速', required=True)
    generator_type = fields.Char(u'发电机类型', required=True)
    rated_power = fields.Float(u'额定功率')
    voltage = fields.Float(u'额定电压', required=True)
    frequency = fields.Float(u'频率', required=True)
    tower_type = fields.Char(u'塔筒类型')
    tower_weight = fields.Float(u'塔筒重量', )
    pneumatic_brake = fields.Char(u'安全制动类型')
    mechanical_brake = fields.Char(u'机械制动类型')
    three_second_maximum = fields.Char(u'生存风速', required=True)
