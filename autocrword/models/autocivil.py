# -*- coding: utf-8 -*-

from odoo import models, fields, api


class civil_specialty(models.Model):
    _name = 'autoreport.civil'
    _description = 'Civil input'
    _rec_name = 'project_id'
    project_id = fields.Many2one('autoreport.project', string='项目名', required=True)
    version_id = fields.Char(u'版本', required=True, default="1.0")
    fort_intensity = fields.Selection([(6, "6"), (7, "7"), (8, "8"), (9, "9")], string=u"设防烈度", required=True)
    beating_capacity = fields.Selection([(60, "60"), (80, "80"), (100, "100"), (120, "120"), (140, "140"), (160, "160"), (180, "180"), (200, "200"), (220, "220"), (240, "240"), (260, "260")], string=u"地基承载力(kpa)", required=True)
    base_form = fields.Selection([('sf',u'扩展基础'), ('ppcf', u'预制承台基础'), ('cpcf', u'灌注桩承台基础'), ('cf', u'复合地基')], string=u'基础形式', required=True)
    ultimate_load = fields.Selection([(50000, "50000"), (60000, "60000"), (70000, "70000"), (80000, "80000"), (90000, "90000"), (100000, "100000"), (110000, "110000"), (120000, "120000")], string=u"极限载荷", required=True)
    Earthrock_ratio= fields.Selection([(0, "0"), (1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5"), (6,  "6"), (7, "7"), (8, "8"), (9, "9"), (10, '10')], string=u"土石方比", required=True)

    @api.multi
    def button_civil(self):
        projectname = self.project_id
        projectname.civil_attachment_id = self
        projectname.civil_attachment_ok = u"已提交,版本：" + self.version_id
        return True
