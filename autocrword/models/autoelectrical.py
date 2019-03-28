# -*- coding: utf-8 -*-

from odoo import models, fields, api
from doc_6 import generate_electrical_docx
import base64


class electrical_specialty(models.Model):
    _name = 'autoreport.electrical'
    _description = 'electrical input'
    _rec_name = 'project_id'
    project_id = fields.Many2one('autoreport.project', string='项目名', required=True)
    version_id = fields.Char(u'版本', required=True, default="1.0")
    voltage_class = fields.Selection([(0, u"平原"), (1, u"山地")], string=u"地形", required=True)
    lenth_singlejL240 = fields.Float(u'单回线路JL/G1A-240/30长度（km）', required=True)
    lenth_doublejL240 = fields.Float(u'双回线路JL/G1A-240/30长度（km）', required=True)
    yjlv95 = fields.Float(u'直埋电缆YJLV22-26/35-3×95（km）', required=True)
    yjv300 = fields.Float(u'直埋电缆YJV22-26/35-1×300（km）', required=True)
    turbine_numbers = fields.Char(u'机位数', default="待提交", readonly=True)

    circuit_number = fields.Integer(u'线路回路数', required=True)
    report_attachment_id = fields.Many2one('ir.attachment', string=u'可研报告电气章节')

    line_1 = fields.Float(u'线路总挖方', required=True)
    line_2 = fields.Float(u'线路总填方', required=True)
    overhead_line = fields.Float(u'架空线路用地', required=True)
    direct_buried_cable = fields.Float(u'直埋电缆用地', required=True)
    overhead_line_num = fields.Float(u'架空线路塔基数量', required=True)
    direct_buried_cable_num = fields.Float(u'直埋电缆长度', required=True)
    main_booster_station_num = fields.Float(u'主变数量', required=True)

    @api.multi
    def electrical_generate(self):
        args = [self.lenth_singlejL240, self.lenth_doublejL240, self.yjlv95, self.yjv300,
                int(self.turbine_numbers), self.circuit_number]
        generate_electrical_docx(self.voltage_class, args)
        reportfile_name = open(
            file=r'C:\Users\Administrator\PycharmProjects\Odoo_addons_NB2\autocrword\models\source\chapter_6\result_chapter6.docx',
            mode='rb')
        byte = reportfile_name.read()
        reportfile_name.close()
        print('file lenth=', len(byte))
        base64.standard_b64encode(byte)
        if (str(self.report_attachment_id) == 'ir.attachment()'):
            Attachments = self.env['ir.attachment']
            print('开始创建新纪录')
            New = Attachments.create({
                'name': self.project_id.project_name + '可研报告电气章节下载页',
                'datas_fname': self.project_id.project_name + '可研报告电气章节.docx',
                'datas': base64.standard_b64encode(byte),
                'display_name': self.project_id.project_name + '可研报告电气章节',
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

    @api.multi
    def button_electrical(self):
        projectname = self.project_id
        myself = self
        projectname.electrical_attachment_id = myself
        projectname.electrical_attachment_ok = u"已提交,版本：" + self.version_id

        projectname.line_1 = self.line_1
        projectname.line_2 = self.line_2
        projectname.overhead_line = self.overhead_line
        projectname.direct_buried_cable = self.direct_buried_cable
        projectname.overhead_line_num = self.overhead_line_num
        projectname.direct_buried_cable_num = self.direct_buried_cable_num
        projectname.main_booster_station_num = self.main_booster_station_num

        projectname.turbine_numbers = self.turbine_numbers
        projectname.voltage_class = self.voltage_class
        projectname.lenth_singlejL240 = self.lenth_singlejL240
        projectname.lenth_doublejL240 = self.lenth_doublejL240
        projectname.yjlv95 = self.yjlv95
        projectname.yjv300 = self.yjv300
        projectname.circuit_number = self.circuit_number

        return True

    def electrical_refresh(self):
        projectname = self.project_id
        self.turbine_numbers = projectname.turbine_numbers_wind
