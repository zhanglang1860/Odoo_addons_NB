# -*- coding: utf-8 -*-

from doc_8 import generate_civil_docx, get_dict_8
import base64
import numpy
from autowind import windenergy_specialty
from odoo import models, fields, api


class civil_specialty(models.Model):
    _name = 'autoreport.civil'
    _description = 'Civil input'
    _rec_name = 'project_id'
    project_id = fields.Many2one('autoreport.project', string='项目名', required=True)
    version_id = fields.Char(u'版本', required=True, default="1.0")
    turbine_numbers = fields.Char(u'机位数', default="待提交", readonly=True)
    report_attachment_id = fields.Many2one('ir.attachment', string=u'可研报告土建章节')
    basic_type = fields.Selection(
        [('扩展基础', u'扩展基础'), ('预制桩承台基础', u'预制桩承台基础'), ('灌注桩承台基础', u'灌注桩承台基础'), ('复合地基', u'复合地基')],
        string=u'基础形式', required=True)
    ultimate_load = fields.Selection(
        [(50000, "50000"), (60000, "60000"), (70000, "70000"), (80000, "80000"), (90000, "90000"), (100000, "100000"),
         (110000, "110000"), (120000, "120000")], string=u"极限载荷", required=True)
    fortification_intensity = fields.Selection([(6, "6"), (7, "7"), (8, "8"), (9, "9")], string=u"设防烈度", required=True)
    basic_earthwork_ratio = fields.Selection(
        [(0, "0"), (1, "10%"), (2, "20%"), (3, "30%"), (4, "40%"), (5, "50%"), (6, "60%"), (7, "70%"),
         (8, "80%"), (9, "90%"), (1, '100%')], string=u"基础土方比", required=True)
    basic_stone_ratio = fields.Selection(
        [(0, "0"), (1, "10%"), (2, "20%"), (3, "30%"), (4, "40%"), (5, "50%"), (6, "60%"), (7, "70%"),
         (8, "80%"), (9, "90%"), (1, '100%')], string=u"基础石方比", required=True)
    road_earthwork_ratio = fields.Selection(
        [(0, "0"), (1, "10%"), (2, "20%"), (3, "30%"), (4, "40%"), (5, "50%"), (6, "60%"), (7, "70%"),
         (8, "80%"), (9, "90%"), (1, '100%')], string=u"道路土方比", required=True)
    road_stone_ratio = fields.Selection(
        [(0, "0"), (1, "10%"), (2, "20%"), (3, "30%"), (4, "40%"), (5, "50%"), (6, "60%"), (7, "70%"),
         (8, "80%"), (9, "90%"), (1, '100%')], string=u"道路石方比", required=True)
    ####箱变
    TurbineCapacity = fields.Selection(
        [(2, "2MW"), (2.2, "2.2MW"), (2.5, "2.5MW"), (3, "3MW"), (3.2, "3.2MW"), (3.3, "3.3MW"), (3.4, "3.4MW"),
         (3.6, "3.6MW")], string=u"风机容量", required=True)
    ####升压站
    Status = fields.Selection([("新建", u"新建"), ("利用原有", u"利用原有")], string=u"升压站状态", required=True)
    Grade = fields.Selection([(110, "110"), (220, "220")], string=u"升压站等级", required=True)
    Capacity = fields.Selection([(50, "50"), (100, "100"), (150, "150"), (200, "200")], string=u"升压站容量", required=True)

    ####道路
    TerrainType = fields.Selection(
        [("平原", u"平原"), ("丘陵", u"丘陵"), ("缓坡低山", u"缓坡低山"), ("陡坡低山", u"陡坡低山"), ("缓坡中山", u"缓坡中山"),
         ("陡坡中山", u"陡坡中山"), ("缓坡高山", u"缓坡高山"), ("陡坡高山", u"陡坡高山")], string=u"山地类型", required=True)

    road_1_num = fields.Float(u'场外改扩建道路', required=True, default=0)
    road_2_num = fields.Float(u'进站道路', required=True, default=0)
    road_3_num = fields.Float(u'施工检修道路工程', required=True, default=0)

    ####线路

    line_1 = fields.Char(u'线路总挖方', default="待提交", readonly=True)
    line_2 = fields.Char(u'线路总填方', default="待提交", readonly=True)
    overhead_line = fields.Char(u'架空线路用地', default="待提交", readonly=True)
    direct_buried_cable = fields.Char(u'直埋电缆用地', default="待提交", readonly=True)
    overhead_line_num = fields.Char(u'架空线路塔基数量', default="待提交", readonly=True)
    direct_buried_cable_num = fields.Char(u'直埋电缆长度', default="待提交", readonly=True)
    main_booster_station_num = fields.Char(u'主变数量', default="待提交", readonly=True)

    @api.multi
    def button_civil(self):
        projectname = self.project_id
        projectname.civil_attachment_id = self
        projectname.civil_attachment_ok = u"已提交,版本：" + self.version_id

        projectname.road_1_num = self.road_1_num
        projectname.road_2_num = self.road_2_num
        projectname.road_3_num = self.road_3_num

        projectname.basic_type = self.basic_type
        projectname.ultimate_load = self.ultimate_load
        projectname.fortification_intensity = self.fortification_intensity
        projectname.basic_earthwork_ratio = str(self.basic_earthwork_ratio * 10) + "%"
        projectname.basic_stone_ratio = str(self.basic_stone_ratio * 10) + "%"
        projectname.TurbineCapacity = self.TurbineCapacity
        projectname.road_earthwork_ratio = str(self.road_earthwork_ratio * 10) + "%"
        projectname.road_stone_ratio = str(self.road_stone_ratio * 10) + "%"
        projectname.Status = self.Status
        projectname.Grade = self.Grade
        projectname.Capacity = self.Capacity
        projectname.TerrainType = self.TerrainType

        projectname.turbine_numbers_civil = self.turbine_numbers

        return True

    def civil_refresh(self):
        projectname = self.project_id
        self.turbine_numbers = projectname.turbine_numbers_wind

        self.line_1 = projectname.line_1
        self.line_2 = projectname.line_2
        self.overhead_line = projectname.overhead_line
        self.direct_buried_cable = projectname.direct_buried_cable
        self.overhead_line_num = projectname.overhead_line_num
        self.direct_buried_cable_num = projectname.direct_buried_cable_num
        self.main_booster_station_num = projectname.main_booster_station_num

        return True

    def civil_generate(self):
        self.line_data = [float(self.line_1), float(self.line_2)]
        self.numbers_list_road = [self.road_1_num, self.road_2_num, self.road_3_num, int(self.turbine_numbers)]
        list = [int(self.turbine_numbers), self.basic_type, self.ultimate_load, self.fortification_intensity,
                self.basic_earthwork_ratio / 10, self.basic_stone_ratio / 10, self.TurbineCapacity,
                self.road_earthwork_ratio / 10,
                self.road_stone_ratio / 10, self.Status, self.Grade, self.Capacity, self.TerrainType,
                self.numbers_list_road,
                float(self.overhead_line), float(self.direct_buried_cable), self.line_data,
                float(self.main_booster_station_num),
                float(self.overhead_line_num), float(self.direct_buried_cable_num)]
        np = numpy.array(list)
        dict_keys = ['turbine_numbers', 'basic_type', 'ultimate_load', 'fortification_intensity',
                     'basic_earthwork_ratio',
                     'basic_stone_ratio', 'TurbineCapacity', 'road_earthwork_ratio', 'road_stone_ratio', 'Status',
                     'Grade', 'Capacity', 'TerrainType', 'numbers_list_road', 'overhead_line', 'direct_buried_cable',
                     'line_data', 'main_booster_station_num', 'overhead_line_num', 'direct_buried_cable_num']

        dict_8 = get_dict_8(np, dict_keys)
        print(dict_8)
        generate_civil_docx(**dict_8)
        reportfile_name = open(
            file=r'C:\Users\Administrator\PycharmProjects\Odoo_addons_NB2\autocrword\models\source\chapter_8\result_chapter8.docx',
            mode='rb')
        byte = reportfile_name.read()
        reportfile_name.close()
        print('file lenth=', len(byte))
        base64.standard_b64encode(byte)
        if (str(self.report_attachment_id) == 'ir.attachment()'):
            Attachments = self.env['ir.attachment']
            print('开始创建新纪录')
            New = Attachments.create({
                'name': self.project_id.project_name + '可研报告土建章节下载页',
                'datas_fname': self.project_id.project_name + '可研报告土建章节.docx',
                'datas': base64.standard_b64encode(byte),
                'display_name': self.project_id.project_name + '可研报告土建章节',
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


class civil_windbase(models.Model):
    _name = 'civil.windbase'
    _description = 'Civil windbase'
    FortificationIntensity = fields.Selection([(6, "6"), (7, "7"), (8, "8"), (9, "9")], string=u"设防烈度", required=True)
    BearingCapacity = fields.Selection(
        [(60, "60"), (80, "80"), (100, "100"), (120, "120"), (140, "140"), (160, "160"), (180, "180"), (200, "200"),
         (220, "220"), (240, "240"), (260, "260")], string=u"地基承载力(kpa)", required=True)
    BasicType = fields.Selection(
        [('扩展基础', u'扩展基础'), ('预制桩承台基础', u'预制桩承台基础'), ('灌注桩承台基础', u'灌注桩承台基础'), ('复合地基', u'复合地基')],
        string=u'基础形式', required=True)
    UltimateLoad = fields.Selection(
        [(50000, "50000"), (60000, "60000"), (70000, "70000"), (80000, "80000"), (90000, "90000"),
         (100000, "100000"), (110000, "110000"), (120000, "120000")], string=u"极限载荷", required=True)
    FloorRadiusR = fields.Float(u'底板半径R')
    R1 = fields.Float(u'棱台顶面半径R1')
    R2 = fields.Float(u'台柱半径R2')
    H1 = fields.Float(u'底板外缘高度H1')
    H2 = fields.Float(u'底板棱台高度H2')
    H3 = fields.Float(u'台柱高度H3')
    PileDiameter = fields.Float(u'桩直径')
    Number = fields.Float(u'根数')
    Length = fields.Float(u'长度')
    SinglePileLength = fields.Float(u'单台总桩长')
    Area = fields.Float(u'面积m2')
    Volume = fields.Float(u'体积m3')
    Cushion = fields.Float(u'垫层')
    M48PreStressedAnchor = fields.Float(u'M48预应力锚栓（m)')
    C80SecondaryGrouting = fields.Float(u'C80二次灌浆')


class civil_convertbase(models.Model):
    _name = 'civil.convertbase'
    _description = 'Civil convertbase'
    TurbineCapacity = fields.Selection(
        [(2, "2MW"), (2.2, "2.2MW"), (2.5, "2.5MW"), (3, "3MW"), (3.2, "3.2MW"), (3.3, "3.3MW"), (3.4, "3.4MW"),
         (3.6, "3.6MW")], string=u"风机容量", required=True)
    ConvertStation = fields.Selection(
        [(2200, "2200"), (2500, "2500"), (2750, "2750"), (3300, "3300"), (3520, "3520"), (4000, "4000")],
        string=u"箱变容量", required=True)

    Long = fields.Float(u'长')
    Width = fields.Float(u'宽')
    High = fields.Float(u'高')
    WallThickness = fields.Float(u'壁厚')
    HighPressure = fields.Float(u'压顶高')
    C35ConcreteTop = fields.Float(u'C35混凝土压顶')
    C15Cushion = fields.Float(u'C15垫层')
    MU10Brick = fields.Float(u'MU10砖')
    Reinforcement = fields.Float(u'钢筋')
    Area = fields.Float(u'面积')


class civil_boosterstation(models.Model):
    _name = 'civil.boosterstation'
    _description = 'Civil boosterstation'
    Status = fields.Selection([("新建", u"新建"), ("利用原有", u"利用原有")], string=u"状态", required=True)
    Grade = fields.Selection([(110, "110"), (220, "220")], string=u"等级", required=True)
    Capacity = fields.Selection([(50, "50"), (100, "100"), (150, "150"), (200, "200")], string=u"容量", required=True)
    Long = fields.Float(u'长')
    Width = fields.Float(u'宽')
    InnerWallArea = fields.Float(u'围墙内面积')
    WallLength = fields.Float(u'围墙长度')
    StoneMasonryFoot = fields.Float(u'浆砌石护脚')
    StoneMasonryDrainageDitch = fields.Float(u'浆砌石排水沟')
    RoadArea = fields.Float(u'道路面积')
    GreenArea = fields.Float(u'绿化面积')
    ComprehensiveBuilding = fields.Float(u'综合楼')
    EquipmentBuilding = fields.Float(u'设备楼')
    AffiliatedBuilding = fields.Float(u'附属楼')
    C30Concrete = fields.Float(u'主变基础C30混凝土')
    C15ConcreteCushion = fields.Float(u'C15混凝土垫层')
    MainTransformerFoundation = fields.Float(u'主变压器基础钢筋')
    AccidentOilPoolC30Concrete = fields.Float(u'事故油池C30混凝土')
    AccidentOilPoolC15Cushion = fields.Float(u'事故油池C15垫层')
    AccidentOilPoolReinforcement = fields.Float(u'事故油池钢筋')
    FoundationC25Concrete = fields.Float(u'设备及架构基础C25混凝土')
    OutdoorStructure = fields.Float(u'室外架构（型钢）')
    PrecastConcretePole = fields.Float(u'预制混凝土杆')
    LightningRod = fields.Float(u'避雷针')


class civil_road1(models.Model):
    _name = 'civil.road1'
    _description = 'Civil road1'
    TerrainType = fields.Selection(
        [("平原", u"平原"), ("丘陵", u"丘陵"), ("缓坡低山", u"缓坡低山"), ("陡坡低山", u"陡坡低山"), ("缓坡中山", u"缓坡中山"),
         ("陡坡中山", u"陡坡中山"), ("缓坡高山", u"缓坡高山"), ("陡坡高山", u"陡坡高山")], string=u"山地类型", required=True)

    GradedGravelPavement_1 = fields.Float(u'级配碎石路面(20cm厚)')
    RoundTubeCulvert_1 = fields.Float(u'D1000mm圆管涵')
    StoneMasonryDrainageDitch_1 = fields.Float(u'浆砌石排水沟')
    MortarStoneRetainingWall_1 = fields.Float(u'M7.5浆砌片石挡墙')
    TurfSlopeProtection_1 = fields.Float(u'草皮护坡')


class civil_road2(models.Model):
    _name = 'civil.road2'
    _description = 'Civil road2'
    TerrainType = fields.Selection(
        [("平原", u"平原"), ("丘陵", u"丘陵"), ("缓坡低山", u"缓坡低山"), ("陡坡低山", u"陡坡低山"), ("缓坡中山", u"缓坡中山"),
         ("陡坡中山", u"陡坡中山"), ("缓坡高山", u"缓坡高山"), ("陡坡高山", u"陡坡高山")], string=u"山地类型", required=True)
    GradedGravelBase_2 = fields.Float(u'级配碎石基层(20cm厚)')
    C30ConcretePavement_2 = fields.Float(u'C30混凝土路面(20cm厚)')
    RoundTubeCulvert_2 = fields.Float(u'D1000mm圆管涵')
    StoneMasonryDrainageDitch_2 = fields.Float(u'浆砌石排水沟')
    MortarStoneRetainingWall_2 = fields.Float(u'M7.5浆砌片石挡墙')
    TurfSlopeProtection_2 = fields.Float(u'草皮护坡')
    Signage_2 = fields.Float(u'标志标牌')
    WaveGuardrail_2 = fields.Float(u'波形护栏')


class civil_road3(models.Model):
    _name = 'civil.road3'
    _description = 'Civil road3'
    TerrainType = fields.Selection(
        [("平原", u"平原"), ("丘陵", u"丘陵"), ("缓坡低山", u"缓坡低山"), ("陡坡低山", u"陡坡低山"), ("缓坡中山", u"缓坡中山"),
         ("陡坡中山", u"陡坡中山"), ("缓坡高山", u"缓坡高山"), ("陡坡高山", u"陡坡高山")], string=u"山地类型", required=True)
    MountainPavement_3 = fields.Float(u'山皮石路面(20cm厚)')
    C30ConcretePavement_3 = fields.Float(u'C30混凝土路面(20cm厚)')
    RoundTubeCulvert_3 = fields.Float(u'D1000mm圆管涵')
    StoneMasonryDrainageDitch_3 = fields.Float(u'浆砌石排水沟')
    MortarStoneRetainingWall_3 = fields.Float(u'M7.5浆砌片石挡墙')
    TurfSlopeProtection_3 = fields.Float(u'草皮护坡')
    Signage_3 = fields.Float(u'标志标牌')
    WaveGuardrail_3 = fields.Float(u'波形护栏')
    LandUse_3 = fields.Float(u'用地')


class civil_road4(models.Model):
    _name = 'civil.road4'
    _description = 'Civil road4'
    TerrainType = fields.Selection(
        [("平原", u"平原"), ("丘陵", u"丘陵"), ("缓坡低山", u"缓坡低山"), ("陡坡低山", u"陡坡低山"), ("缓坡中山", u"缓坡中山"),
         ("陡坡中山", u"陡坡中山"), ("缓坡高山", u"缓坡高山"), ("陡坡高山", u"陡坡高山")], string=u"山地类型", required=True)
    GeneralSiteLeveling_4 = fields.Float(u'一般场地平整')
    StoneMasonryDrainageDitch_4 = fields.Float(u'浆砌石排水沟')
    MortarStoneProtectionSlope_4 = fields.Float(u'M7.5浆砌片石护坡')
    TurfSlopeProtection_4 = fields.Float(u'草皮护坡')
