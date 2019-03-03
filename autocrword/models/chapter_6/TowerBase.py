from TowerType import TowerType
from RoundUp import round_up
from Cable import Cable


class TowerBase(TowerType):
    """
    铁塔基础
    """

    def __init__(self, *value_list):
        TowerType.__init__(self, *value_list)
        self.used_numbers_base_type = ''
        self.used_numbers_base_sum = 0
        self.c25_unit_list = []
        self.c25_unit_zjc1, self.c25_unit_zjc2, self.c25_unit_jjc1 = 0, 0, 0
        self.c25_unit_jjc2, self.c25_unit_tw1, self.c25_unit_tw2 = 0, 0, 0
        self.c25_unit_layer, self.c25_unit = 0, 0
        self.c25_sum_zjc1, self.c25_sum_zjc2, self.c25_sum_jjc1 = 0, 0, 0
        self.c25_sum_jjc2, self.c25_sum_tw1, self.c25_sum_tw2 = 0, 0, 0
        self.c25_sum_layer, self.c25_sum = 0, 0

        self.steel_unit_list = []
        self.steel_unit_zjc1, self.steel_unit_zjc2, self.steel_unit_jjc1 = 0, 0, 0
        self.steel_unit_jjc2, self.steel_unit_tw1, self.steel_unit_tw2 = 0, 0, 0
        self.steel_unit_layer, self.steel_unit = 0, 0
        self.steel_sum_zjc1, self.steel_sum_zjc2, self.steel_sum_jjc1 = 0, 0, 0
        self.steel_sum_jjc2, self.steel_sum_tw1, self.steel_sum_tw2 = 0, 0, 0
        self.steel_sum_layer, self.steel_sum = 0, 0

        self.foot_bolt_list = []
        self.foot_bolt_unit_zjc1, self.foot_bolt_unit_zjc2, self.foot_bolt_unit_jjc1 = 0, 0, 0
        self.foot_bolt_unit_jjc2, self.foot_bolt_unit_tw1, self.foot_bolt_unit_tw2 = 0, 0, 0
        self.foot_bolt_unit_layer, self.foot_bolt_unit = 0, 0
        self.foot_bolt_sum_zjc1, self.foot_bolt_sum_zjc2, self.foot_bolt_sum_jjc1 = 0, 0, 0
        self.foot_bolt_sum_jjc2, self.foot_bolt_sum_tw1, self.foot_bolt_sum_tw2 = 0, 0, 0
        self.foot_bolt_sum_layer, self.foot_bolt_sum = 0, 0

        self.used_numbers_base_type_list = []
        self.used_numbers_base_zjc1, self.used_numbers_base_zjc2, self.used_numbers_base_jjc1 = 0, 0, 0
        self.used_numbers_base_jjc2, self.used_numbers_base_tw1, self.used_numbers_base_tw2 = 0, 0, 0
        self.used_numbers_base_layer = 0

    def electrical_insulator_model(self, base_type, c25_unit, steel_unit, foot_bolt_unit):
        self.used_numbers_base_type = base_type
        self.c25_unit = c25_unit
        self.steel_unit = steel_unit
        self.foot_bolt_unit = foot_bolt_unit
        if self.used_numbers_base_type == "ZJC1":
            self.used_numbers_base_zjc1 = round_up(
                (self.used_numbers_single_Z2_30 + self.used_numbers_double_SZ2_30) / 2, 0)
            self.c25_unit_zjc1 = self.c25_unit
            self.c25_sum_zjc1 = self.used_numbers_base_zjc1 * self.c25_unit_zjc1
            self.steel_unit_zjc1 = self.steel_unit
            self.steel_sum_zjc1 = self.used_numbers_base_zjc1 * self.steel_unit_zjc1 / 1000
            self.foot_bolt_unit_zjc1 = self.foot_bolt_unit
            self.foot_bolt_sum_zjc1 = self.used_numbers_base_zjc1 * self.foot_bolt_unit_zjc1

        if self.used_numbers_base_type == "ZJC2":
            self.used_numbers_base_zjc2 = round_up(
                (self.used_numbers_single_ZK_42 + self.used_numbers_double_SZK_42) / 2, 0)
            self.c25_unit_zjc2 = self.c25_unit
            self.c25_sum_zjc2 = self.used_numbers_base_zjc2 * self.c25_unit_zjc2
            self.steel_unit_zjc2 = self.steel_unit
            self.steel_sum_zjc2 = self.used_numbers_base_zjc2 * self.steel_unit_zjc2 / 1000
            self.foot_bolt_unit_zjc2 = self.foot_bolt_unit
            self.foot_bolt_sum_zjc2 = self.used_numbers_base_zjc2 * self.foot_bolt_unit_zjc2

        if self.used_numbers_base_type == "JJC1":
            self.used_numbers_base_jjc1 = self.used_numbers_single_J2_24 + self.used_numbers_double_SJ2_24
            self.c25_unit_jjc1 = self.c25_unit
            self.c25_sum_jjc1 = self.used_numbers_base_jjc1 * self.c25_unit_jjc1
            self.steel_unit_jjc1 = self.steel_unit
            self.steel_sum_jjc1 = self.used_numbers_base_jjc1 * self.steel_unit_jjc1 / 1000
            self.foot_bolt_unit_jjc1 = self.foot_bolt_unit
            self.foot_bolt_sum_jjc1 = self.used_numbers_base_jjc1 * self.foot_bolt_unit_jjc1

        if self.used_numbers_base_type == "JJC2":
            self.used_numbers_base_jjc2 = self.used_numbers_single_J4_24 + self.used_numbers_single_FS_18 \
                                          + self.used_numbers_double_SJ4_24
            self.c25_unit_jjc2 = self.c25_unit
            self.c25_sum_jjc2 = self.used_numbers_base_jjc2 * self.c25_unit_jjc2
            self.steel_unit_jjc2 = self.steel_unit
            self.steel_sum_jjc2 = self.used_numbers_base_jjc2 * self.steel_unit_jjc2 / 1000
            self.foot_bolt_unit_jjc2 = self.foot_bolt_unit
            self.foot_bolt_sum_jjc2 = self.used_numbers_base_jjc2 * self.foot_bolt_unit_jjc2

        if self.used_numbers_base_type == "TW1":
            self.used_numbers_base_tw1 = self.used_numbers_single_Z2_30 + self.used_numbers_double_SZ2_30 \
                                         - self.used_numbers_base_zjc1
            self.c25_unit_tw1 = self.c25_unit
            self.c25_sum_tw1 = round_up((self.used_numbers_base_tw1 * self.c25_unit_tw1),2)
            self.steel_unit_tw1 = self.steel_unit
            self.steel_sum_tw1 = self.used_numbers_base_tw1 * self.steel_unit_tw1 / 1000
            self.foot_bolt_unit_tw1 = self.foot_bolt_unit
            self.foot_bolt_sum_tw1 = self.used_numbers_base_tw1 * self.foot_bolt_unit_tw1

        if self.used_numbers_base_type == "TW2":
            self.used_numbers_base_tw2 = self.used_numbers_single_ZK_42 + self.used_numbers_double_SZK_42 \
                                         - self.used_numbers_base_zjc2
            self.c25_unit_tw2 = self.c25_unit
            self.c25_sum_tw2 = round_up((self.used_numbers_base_tw2 * self.c25_unit_tw2),2)
            self.steel_unit_tw2 = self.steel_unit
            self.steel_sum_tw2 = self.used_numbers_base_tw2 * self.steel_unit_tw2 / 1000
            self.foot_bolt_unit_tw2 = self.foot_bolt_unit
            self.foot_bolt_sum_tw2 = self.used_numbers_base_tw2 * self.foot_bolt_unit_tw2

        if self.used_numbers_base_type == "基础垫层":
            self.used_numbers_base_layer = self.sum_used_numbers
            self.c25_unit_layer = self.c25_unit
            self.c25_sum_layer = self.used_numbers_base_layer * self.c25_unit_layer
            self.steel_unit_layer = self.steel_unit
            self.steel_sum_layer = self.used_numbers_base_layer * self.steel_unit_layer / 1000
            self.foot_bolt_unit_layer = self.foot_bolt_unit
            self.foot_bolt_sum_layer = self.used_numbers_base_layer * self.foot_bolt_unit_layer

    def sum_cal_tower_base(self, tower_base_li, c25_unit_li, steel_unit_li, foot_bolt_li):
        self.c25_unit_list = c25_unit_li
        self.used_numbers_base_type_list = tower_base_li
        self.steel_unit_list = steel_unit_li
        self.foot_bolt_list = foot_bolt_li
        for i in range(0, len(self.c25_unit_list)):
            TowerBase.electrical_insulator_model(self, self.used_numbers_base_type_list[i], self.c25_unit_list[i],
                                                 self.steel_unit_list[i], foot_bolt_list[i])

        self.used_numbers_base_sum = round_up((self.used_numbers_base_zjc1 + self.used_numbers_base_zjc2 +
                                               self.used_numbers_base_jjc1 + self.used_numbers_base_jjc2 +
                                               self.used_numbers_base_tw1 + self.used_numbers_base_tw2), 2)
        self.c25_sum = round_up((self.c25_sum_zjc1 + self.c25_sum_zjc2 + self.c25_sum_jjc1 + self.c25_sum_jjc2 +
                                 self.c25_sum_tw1 + self.c25_sum_tw2 + self.c25_sum_layer), 2)
        self.steel_sum = round_up((self.steel_sum_zjc1 + self.steel_sum_zjc2 + self.steel_sum_jjc1 + self.steel_sum_jjc2
                                   + self.steel_sum_tw1 + self.steel_sum_tw2 + self.steel_sum_layer), 2)

        self.foot_bolt_sum = round_up((self.foot_bolt_sum_zjc1 + self.foot_bolt_sum_zjc2 + self.foot_bolt_sum_jjc1 +
                                       self.foot_bolt_sum_jjc2), 2)
        # print(self.tower_type, self.tower_type_high, self.used_numbers)


tower_type_list = ['单回耐张塔', '单回耐张塔', '单回耐张塔', '单回直线塔', '单回直线塔', '双回耐张塔', '双回耐张塔', '双回直线塔', '双回直线塔', '铁塔电缆支架']
tower_type_high_list = ['J2-24', 'J4-24', 'FS-18', 'Z2-30', 'ZK-42', 'SJ2-24', 'SJ4-24', 'SZ2-30', 'SZK-42', '角钢']
tower_weight_list = [6.8, 8.5, 7, 5.5, 8.5, 12.5, 17, 6.5, 10, 0.5, ]
tower_height_list = [32, 32, 27, 37, 49, 37, 37, 42, 54, 0]
tower_foot_distance_list = [5.5, 5.5, 6, 5, 6, 7, 8, 6, 8, 0]

c25_unit_list = [12, 16, 42, 80, 8.8, 10.2, 2.4]
steel_unit_list = [300, 500, 750, 900, 600, 800, 0]
foot_bolt_list = [100, 180, 280, 360, 100, 180, 0]

tower_base_list = ['ZJC1', 'ZJC2', 'JJC1', 'JJC2', 'TW1', 'TW2', '基础垫层']
# 需要改成字典形式

project02 = TowerBase(25.3, 23.6, 1.55, 3, 31, 5)
project02.sum_cal_tower_type(tower_type_list, tower_type_high_list, tower_weight_list, tower_height_list,
                             tower_foot_distance_list)

project02.sum_cal_tower_base(tower_base_list, c25_unit_list, steel_unit_list, foot_bolt_list)

print(project02.foot_bolt_sum_zjc1, project02.foot_bolt_sum_zjc2, project02.foot_bolt_sum_jjc1,
      project02.foot_bolt_sum_jjc2,
      project02.foot_bolt_sum_tw1, project02.foot_bolt_sum_tw2,
      project02.foot_bolt_sum_layer, project02.foot_bolt_sum)

cable_project_list = ['高压电缆', '高压电缆', '电缆沟', '电缆终端', '电缆终端']
cable_model_list = ['YJLV22-26/35-3×95', 'YJV22-26/35-1×300', '电缆沟长度', 'YJLV22-26/35-3×95', 'YJV22-26/35-1×300']
project03 = Cable(25.3, 23.6, 1.55, 3, 31, 5)
project03.sum_cal_cable(cable_project_list, cable_model_list)
print(project03.cable_model_YJLV22_26_35_3_95_gaoya, project03.cable_model_YJV22_26_35_1_300_gaoya,
      project03.cable_model_cable_duct,
      project03.cable_model_YJLV22_26_35_3_95_dianlanzhongduan, project03.cable_model_YJV22_26_35_1_300_dianlanzhongduan)
