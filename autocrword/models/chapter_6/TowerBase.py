from TowerType import TowerType
from RoundUp import round_up


class TowerBase(TowerType):
    def __init__(self, *value_list):
        TowerType.__init__(self, *value_list)

        self.used_numbers_base_zjc1 = 0
        self.used_numbers_base_zjc2 = 0
        self.used_numbers_base_jjc1 = 0
        self.used_numbers_base_jjc2 = 0
        self.used_numbers_base_tw1 = 0
        self.used_numbers_base_tw2 = 0
        self.used_numbers_base_layer = 0

    def electrical_insulator_model(self, base_zjc1, base_zjc2, base_jjc1, base_jjc2, base_tw1, base_tw2, base_layer):
        self.used_numbers_base_zjc1 = base_zjc1
        self.used_numbers_base_zjc2 = base_zjc2
        self.used_numbers_base_jjc1 = base_jjc1
        self.used_numbers_base_jjc2 = base_jjc2
        self.used_numbers_base_tw1 = base_tw1
        self.used_numbers_base_tw2 = base_tw2
        self.used_numbers_base_layer = base_layer

        if self.used_numbers_base_zjc1 == "ZJC1":

            self.used_numbers_base_zjc1 = round_up(
                (self.used_numbers_single_Z2_30 + self.used_numbers_double_SZ2_30) / 2, 0)

        if self.used_numbers_base_zjc2 == "ZJC2":
            self.used_numbers_base_zjc2 = round_up(
                (self.used_numbers_single_ZK_42 + self.used_numbers_double_SZK_42) / 2, 0)

        if self.used_numbers_base_jjc1 == "JJC1":
            self.used_numbers_base_jjc1 = self.used_numbers_single_J2_24 + self.used_numbers_double_SJ2_24

        if self.used_numbers_base_jjc2 == "JJC2":
            self.used_numbers_base_jjc2 = self.used_numbers_single_J4_24 + self.used_numbers_single_FS_18 \
                                          + self.used_numbers_double_SJ4_24

        if self.used_numbers_base_tw1 == "TW1":
            self.used_numbers_base_tw1 = self.used_numbers_single_Z2_30 + self.used_numbers_double_SZ2_30 \
                                         - self.used_numbers_base_zjc1

        if self.used_numbers_base_tw2 == "TW2":
            self.used_numbers_base_tw2 = self.used_numbers_single_ZK_42 + self.used_numbers_double_SZK_42 \
                                         - self.used_numbers_base_zjc2

        if self.used_numbers_base_layer == "基础垫层":
            self.used_numbers_base_layer = self.sum_used_numbers


tower_base_list = ['ZJC1', 'ZJC2', 'JJC1', 'JJC2', 'TW1', 'TW2', '基础垫层']
tower_type_list = ['单回耐张塔', '单回耐张塔', '单回耐张塔', '单回直线塔', '单回直线塔', '双回耐张塔', '双回耐张塔', '双回直线塔', '双回直线塔', '铁塔电缆支架']
tower_type_high_list = ['J2-24', 'J4-24', 'FS-18', 'Z2-30', 'ZK-42', 'SJ2-24', 'SJ4-24', 'SZ2-30', 'SZK-42', '角钢']
tower_weight_list = [6.8, 8.5, 7, 5.5, 8.5, 12.5, 17, 6.5, 10, 0.5, ]
tower_height_list = [32, 32, 27, 37, 49, 37, 37, 42, 54, 0]
tower_foot_distance_list = [5.5, 5.5, 6, 5, 6, 7, 8, 6, 8, 0]

c25_list=[]
project02 = TowerBase(25.3, 23.6, 1.55, 3, 31, 5)


project02.sum_cal(tower_type_list, tower_type_high_list, tower_weight_list, tower_height_list, tower_foot_distance_list)
project02.electrical_insulator_model(*tower_base_list)
print(project02.used_numbers_base_zjc1, project02.used_numbers_base_zjc2, project02.used_numbers_base_jjc1,
      project02.used_numbers_base_jjc2, project02.used_numbers_base_tw1, project02.used_numbers_base_tw2,
      project02.used_numbers_base_layer)
