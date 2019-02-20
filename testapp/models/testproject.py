# -*- coding: utf-8 -*-

from odoo import models, fields, api

class project(models.Model):
    _name = 'test.project'
    _description = 'Project'
    _rec_name = 'project_name'
    project_name = fields.Char('projectname', required=True)
    order_number = fields.Char('number')


    # @api.multi
    # def button_project(self):
    #     renew.read_excel()
    #     msg = "The attribute is not valid."
    #     return True



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