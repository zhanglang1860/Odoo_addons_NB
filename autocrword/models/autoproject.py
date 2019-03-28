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
    project_capacity = fields.Float(u'项目容量', required=True)
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

    staff = fields.Integer(u'工程定员', required=True)

    ###风能
    turbine_numbers_wind = fields.Char(u'机位数', default="待提交", readonly=True)
    ###电气
    line_1 = fields.Char(u'线路总挖方', default="待提交", readonly=True)
    line_2 = fields.Char(u'线路总填方', default="待提交", readonly=True)
    overhead_line = fields.Char(u'架空线路用地', default="待提交", readonly=True)
    direct_buried_cable = fields.Char(u'直埋电缆用地', default="待提交", readonly=True)
    overhead_line_num = fields.Char(u'架空线路塔基数量', default="待提交", readonly=True)
    direct_buried_cable_num = fields.Char(u'直埋电缆长度', default="待提交", readonly=True)
    main_booster_station_num = fields.Char(u'主变数量', default="待提交", readonly=True)

    voltage_class = fields.Char(u'地形', default="待提交", readonly=True)
    lenth_singlejL240 = fields.Char(u'单回线路JL/G1A-240/30长度（km）', default="待提交", readonly=True)
    lenth_doublejL240 = fields.Char(u'双回线路JL/G1A-240/30长度（km）', default="待提交", readonly=True)
    yjlv95 = fields.Char(u'直埋电缆YJLV22-26/35-3×95（km）', default="待提交", readonly=True)
    yjv300 = fields.Char(u'直埋电缆YJV22-26/35-1×300（km）', default="待提交", readonly=True)
    circuit_number = fields.Char(u'线路回路数', default="待提交", readonly=True)

    ###土建
    road_1_num = fields.Char(u'场外改扩建道路', default="待提交", readonly=True)
    road_2_num = fields.Char(u'进站道路', default="待提交", readonly=True)
    road_3_num = fields.Char(u'施工检修道路工程', default="待提交", readonly=True)

    basic_type = fields.Char(u'基础形式', default="待提交", readonly=True)
    ultimate_load = fields.Char(u'极限载荷', default="待提交", readonly=True)
    fortification_intensity = fields.Char(u'设防烈度', default="待提交", readonly=True)
    basic_earthwork_ratio = fields.Char(u'基础土方比', default="待提交", readonly=True)
    basic_stone_ratio = fields.Char(u'基础石方比', default="待提交", readonly=True)
    TurbineCapacity = fields.Char(u'风机容量', default="待提交", readonly=True)
    road_earthwork_ratio = fields.Char(u'道路土方比', default="待提交", readonly=True)
    road_stone_ratio = fields.Char(u'道路石方比', default="待提交", readonly=True)
    Status = fields.Char(u'升压站状态', default="待提交", readonly=True)
    Grade = fields.Char(u'升压站等级', default="待提交", readonly=True)
    Capacity = fields.Char(u'升压站容量', default="待提交", readonly=True)
    TerrainType = fields.Char(u'山地类型', default="待提交", readonly=True)

    turbine_numbers_civil = fields.Char(u'机位数', default="待提交", readonly=True)
    turbine_numbers_electric = fields.Char(u'机位数', default="待提交", readonly=True)


    @api.multi
    def button_project(self):

        if(self.turbine_numbers_civil!=self.turbine_numbers_wind):
            pass

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