# -*- coding: utf-8 -*-

# from odoo import models, fields, api


class economic_specialty(models.Model):
    _name = 'autoreport.economic'
    _description = 'economic input'
    _rec_name = 'project_id'
    project_id = fields.Many2one('autoreport.project', string='项目名', required=True)
    version_id = fields.Char(u'版本', required=True, default="1.0")
    economic_main_attachment_id = fields.Many2one('ir.attachment', string=u'经济评价文件')

    @api.multi
    def button_economic(self):
        projectname = self.project_id
        myself = self
        projectname.economic_attachment_id = myself
        projectname.economic_attachment_ok = u"已提交,版本：" + self.version_id
        return True
