# -*- coding: utf-8 -*-

from odoo import models, fields, api
from . import renew2
from odoo import exceptions
import datetime
import base64

class project(models.Model):
    _name = 'autoreport.project'
    _description = 'Project'
    _rec_name = 'project_name'
    project_name = fields.Char(u'项目名', required=True, write=['autocrword.project_group_user'])
    order_number = fields.Char(u'项目编号', required=True)
    announce_capacity = fields.Float(u'项目容量', required=True)
    active = fields.Boolean(u'续存？', default=True)
    date_start = fields.Date(u'项目启动日期', default=fields.date.today())
    dat_end = fields.Date(u'项目要求完成日期',default=fields.date.today()+datetime.timedelta(days=10))
    company_id = fields.Many2one('res.company', string=u'项目所在大区')
    contacts_ids = fields.Many2many('res.partner', string=u'项目联系人')
    favorite_user_ids = fields.Many2many('res.users', string=u'项目组成员')
    message_main_attachment_id = fields.Many2many('ir.attachment', string=u'任务资料')
    wind_attachment_id = fields.Many2one('autoreport.windenergy', string=u'风能数据', groups='autocrword.wind_group_user')
    wind_attachment_ok = fields.Char(u'风能数据', default="待提交", readonly=True)
    electrical_attachment_id = fields.Many2one('autoreport.electrical', string=u'电气数据', groups='autocrword.electrical_group_user')
    electrical_attachment_ok = fields.Char(u'电气数据', default="待提交", readonly=True)
    civil_attachment_id = fields.Many2one('autoreport.civil', string=u'土建数据', groups='autocrword.civil_group_user')
    civil_attachment_ok = fields.Char(u'土建数据', default="待提交", readonly=True)
    economic_attachment_id = fields.Many2one('autoreport.economic', string=u'经评数据', groups='autocrword.economic_group_user')
    economic_attachment_ok = fields.Char(u'经评数据', default="待提交", readonly=True)
    report_attachment_id = fields.Many2one('ir.attachment', string=u'可研报告成果')

    turbine_numbers = fields.Char(u'机位数', default="待提交", readonly=True)
    line_1 = fields.Char(u'线路总挖方', default="待提交", readonly=True)
    line_2 = fields.Char(u'线路总填方', default="待提交", readonly=True)
    overhead_line = fields.Char(u'架空线路用地', default="待提交", readonly=True)
    direct_buried_cable = fields.Char(u'直埋电缆用地', default="待提交", readonly=True)
    overhead_line_num = fields.Char(u'架空线路塔基数量', default="待提交", readonly=True)
    direct_buried_cable_num = fields.Char(u'直埋电缆长度', default="待提交", readonly=True)
    main_booster_station_num = fields.Char(u'主变数量', default="待提交", readonly=True)


    @api.multi
    def button_project(self):
        if(str(self.wind_attachment_id)=='autoreport.wind()'):
            raise exceptions.UserError('该项目风资源资料未上传，请上传后再生成报告。')
        if (str(self.civil_attachment_id) == 'autoreport.civil()'):
            raise exceptions.UserError('该项目土建资料未上传，请上传后再生成报告。')
        if (str(self.electrical_attachment_id) == 'autoreport.electrical()'):
            raise exceptions.UserError('该项目电气资料未上传，请上传后再生成报告。')
        if (str(self.economic_attachment_id) == 'autoreport.economic()'):
            raise exceptions.UserError('该项目经济评价资料未上传，请上传后再生成报告。')

        print('old attachment：', self.report_attachment_id)
        if (str(self.report_attachment_id) != 'ir.attachment()'):print('old datas len：', len(self.report_attachment_id.datas))

        renew2.read_excel()
        reportfile_name = open(file='C:/autoreport/result.docx', mode='rb')
        byte = reportfile_name.read()
        reportfile_name.close()
        print('file lenth=', len(byte))
        base64.standard_b64encode(byte)
        if(str(self.report_attachment_id) == 'ir.attachment()'):
            Attachments = self.env['ir.attachment']
            New = Attachments.create({
                'name': self.project_name+'可研报告下载页',
                'datas_fname': self.project_name+'可研报告.docx',
                'datas':  base64.standard_b64encode(byte),
                'display_name': self.project_name+'可研报告3',
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

    # project_name = fields.Char('Project_name', string=u'项目名', required=True)
    # order_number = fields.Char('Order_number', string=u'项目编号')
    # announce_capacity = fields.Float('Installed Capacity', string=u'项目容量', required=True)
    # active = fields.Boolean('Active?', string=u'续存', default=True)
    # date_start = fields.Date(string=u'起始日期')
    # dat_end = fields.Date(string=u'要求完成日期')
    # company_id = fields.Char('res.company', string=u'项目所在大区')
    # contacts_ids = fields.Many2many('res.partner', string=u'项目联系人')
    # favorite_user_ids = fields.Many2many('res.users', string=u'项目组成员')
    # message_main_attachment_id = fields.Many2one('ir.attachment', string=u'项目任务文档')






    # name = fields.Char()
    # value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100