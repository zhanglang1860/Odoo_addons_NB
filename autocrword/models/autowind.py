# -*- coding: utf-8 -*-

from odoo import models, fields, api
import base64
import doc_5


class windenergy_specialty(models.Model):
    _name = 'autoreport.windenergy'
    _description = 'Wind energy input'
    _rec_name = 'project_id'
    project_id = fields.Many2one('autoreport.project', string=u'项目名', required=True)
    civil_id = fields.Many2one('autoreport.civil', string=u'项目名', required=True)
    version_id = fields.Char(u'版本', required=True, default="1.0")
    turbine_numbers = fields.Integer(u'机位数', required=True)
    generator_ids = fields.Many2many('autoreport.generator', required=True, string=u'比选机型')
    report_attachment_id = fields.Many2one('ir.attachment', string=u'可研报告风能章节')

    @api.multi
    def button_wind(self):
        projectname = self.project_id
        civilname = self.civil_id.turbine_numbers
        windattachmentid = projectname.wind_attachment_id
        myself = self
        projectname.wind_attachment_id = myself
        projectname.wind_attachment_ok = u"已提交,版本：" + self.version_id
        projectname.turbine_numbers = self.turbine_numbers
        civilname = self.turbine_numbers
        return True

    @api.multi
    def wind_generate(self):
        tur_name = []
        for i in range(0, len(self.generator_ids)):
            tur_name.append(self.generator_ids[i].name_tur)
        path_images = r"C:\Users\Administrator\PycharmProjects\Odoo_addons_NB2\autocrword\models\source\chapter_5"

        doc_5.generate_wind_docx(tur_name, path_images)
        ###########################

        reportfile_name = open(
            file=r'C:\Users\Administrator\PycharmProjects\Odoo_addons_NB2\autocrword\models\source\chapter_5\result_chapter5.docx',
            mode='rb')
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
