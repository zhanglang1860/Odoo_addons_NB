# -*- coding: utf-8 -*-

from odoo import models, fields, api


class civil_specialty(models.Model):
    _name = 'autoreport.civil'
    _description = 'Civil input'
    _rec_name = 'project_id'
    project_id = fields.Many2one('autoreport.project', string='项目名', required=True)
    version_id = fields.Char(u'版本', required=True, default="1.0")
    fort_intensity = fields.Selection([(6, "6"), (7, "7"), (8, "8"), (9, "9")], string=u"设防烈度", required=True)
    beating_capacity = fields.Selection(
        [(60, "60"), (80, "80"), (100, "100"), (120, "120"), (140, "140"), (160, "160"), (180, "180"), (200, "200"),
         (220, "220"), (240, "240"), (260, "260")], string=u"地基承载力(kpa)", required=True)
    base_form = fields.Selection([('扩展基础', u'扩展基础'), ('扩展基础', u'扩展基础'), ('灌注桩承台基础', u'灌注桩承台基础'), ('复合地基', u'复合地基')],
                                 string=u'基础形式', required=True)
    ultimate_load = fields.Selection(
        [(50000, "50000"), (60000, "60000"), (70000, "70000"), (80000, "80000"), (90000, "90000"), (100000, "100000"),
         (110000, "110000"), (120000, "120000")], string=u"极限载荷", required=True)
    Earthrock_ratio = fields.Selection(
        [(0, "0"), (1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5"), (6, "6"), (7, "7"), (8, "8"), (9, "9"),
         (10, '10')], string=u"土石方比", required=True)

    @api.multi
    def button_civil(self):
        projectname = self.project_id
        projectname.civil_attachment_id = self
        projectname.civil_attachment_ok = u"已提交,版本：" + self.version_id
        return True


class civil_windbase(models.Model):
    _name = 'civil.windbase'
    _description = 'Civil windbase'
    FortificationIntensity = fields.Selection([(6, "6"), (7, "7"), (8, "8"), (9, "9")], string=u"设防烈度", required=True)
    BearingCapacity = fields.Selection(
        [(60, "60"), (80, "80"), (100, "100"), (120, "120"), (140, "140"), (160, "160"), (180, "180"), (200, "200"),
         (220, "220"), (240, "240"), (260, "260")], string=u"地基承载力(kpa)", required=True)
    BasicType = fields.Selection([('扩展基础', u'扩展基础'), ('预制承台基础', u'预制承台基础'), ('灌注桩承台基础', u'灌注桩承台基础'), ('复合地基', u'复合地基')],
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
        [(2, "2MW"), (2.2, "2.2MW"), (2.5, "2.5MW"), (3, "3MW"),(3.2, "3.2MW"),(3.3, "3.3MW"),(3.4, "3.4MW"),
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
        [("平原", u"平原"), ("丘陵", u"丘陵"), ("缓坡低山", u"缓坡低山"), ("陡坡低山", u"陡坡低山"),("缓坡中山", u"缓坡中山"),
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
