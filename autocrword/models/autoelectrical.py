# -*- coding: utf-8 -*-

from odoo import models, fields, api


class electrical_specialty(models.Model):
    _name = 'autoreport.electrical'
    _description = 'electrical input'
    _rec_name = 'project_id'
    project_id = fields.Many2one('autoreport.project', string='项目名', required=True)
    version_id = fields.Char(u'版本', required=True, default="1.0")
    voltage_class = fields.Selection([('plain', u"平原"), ('mountain', u"山地")], string=u"地形", required=True)
    lenth_singlejL240 = fields.Float(u'单回线路JL/G1A-240/30长度（km）', required=True)
    lenth_doublejL240 = fields.Float(u'双回线路JL/G1A-240/30长度（km）', required=True)
    yjlv95 = fields.Float(u'直埋电缆YJLV22-26/35-3×95（km）', required=True)
    yjv300 = fields.Float(u'直埋电缆YJV22-26/35-1×300（km）', required=True)
    circuit_number = fields.Integer(u'线路回路数', required=True)

    @api.multi
    def button_electrical(self):
        projectname = self.project_id
        myself = self
        projectname.electrical_attachment_id = myself
        projectname.electrical_attachment_ok = u"已提交,版本：" + self.version_id
        return True
