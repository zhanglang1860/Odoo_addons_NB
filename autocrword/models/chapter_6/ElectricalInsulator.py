from ElectricalCircuit import ElectricalCircuit
from TowerType import TowerType


class ElectricalInsulator(TowerType):
    """
    绝缘子
    """

    def __init__(self, *value_list):
        # ElectricalCircuit.__init__(self, *value_list)
        TowerType.__init__(self, *value_list)
        self.electrical_insulator_name = ''
        self.composite_insulator = ''
        self.porcelain_insulator = ''
        self.composite_pin_insulator = ''
        self.composite_zinc_oxide_protector = ''
        self.used_numbers_FXBW4_35_70 = 0
        self.used_numbers_U70BP_146D = 0
        self.used_numbers_FPQ_35_4T16 = 0
        self.used_numbers_YH5WZ_51_134 = 0

    def electrical_insulator_model(self, project_chapter6_type, electrical_insulator_name, electrical_insulator_type):

        self.project_chapter6_type = project_chapter6_type
        self.electrical_insulator_name = electrical_insulator_name
        self.electrical_insulator_type = electrical_insulator_type

        if self.project_chapter6_type == "山区":
            if self.electrical_insulator_name == '复合绝缘子':
                if self.electrical_insulator_type == 'FXBW4_35_70':
                    self.composite_insulator = 'FXBW4_35_70'
            elif self.electrical_insulator_name == '瓷绝缘子':
                if self.electrical_insulator_type == 'U70BP_146D':
                    self.porcelain_insulator = 'U70BP_146D'
            elif self.electrical_insulator_name == '复合针式绝缘子':
                if self.electrical_insulator_type == 'FPQ_35_4T16':
                    self.porcelain_insulator = 'FPQ_35_4T16'
            elif self.electrical_insulator_name == '复合外套氧化锌避雷器':
                if self.electrical_insulator_type == 'YH5WZ_51_134':
                    self.porcelain_insulator = 'YH5WZ_51_134'


            if self.composite_insulator == "FXBW4_35_70":
                self.used_numbers_FXBW4_35_70 = (self.used_numbers_single_Z2_30 + self.used_numbers_single_ZK_42) * 3 + \
                                                (
                                                        self.used_numbers_double_SZ2_30 + self.used_numbers_double_SZK_42) * 3 + \
                                                (
                                                        self.used_numbers_single_J2_24 + self.used_numbers_single_J4_24 + self.used_numbers_single_FS_18) * 4 + \
                                                (
                                                        self.used_numbers_double_SJ2_24 + self.used_numbers_double_SJ4_24) * 6 + \
                                                (
                                                        self.used_numbers_single_J2_24 + self.used_numbers_single_J4_24 + self.used_numbers_single_FS_18) * 12 + \
                                                (self.used_numbers_double_SJ2_24 + self.used_numbers_double_SJ4_24) * 12

            if self.porcelain_insulator == "U70BP_146D":
                self.used_numbers_U70BP_146D = ((
                                                        self.used_numbers_double_SJ2_24 + self.used_numbers_double_SJ4_24) * 12 + \
                                                (
                                                        self.used_numbers_double_SZ2_30 + self.used_numbers_double_SZK_42) * 3) * 5

            if self.composite_pin_insulator == "FPQ_35_4T16":
                self.used_numbers_FPQ_35_4T16 = (self.tur_number + self.line_loop_number) * 12

            if self.composite_zinc_oxide_protector == "YH5WZ_51_134":
                self.used_numbers_YH5WZ_51_134 = (self.tur_number + self.line_loop_number) * 3

# insulator_list = ['FXBW4-35/70', 'U70BP-146D', 'FPQ-35/4T16', 'YH5WZ-51/134']
# tower_type_list = ['单回耐张塔', '单回耐张塔', '单回耐张塔', '单回直线塔', '单回直线塔', '双回耐张塔', '双回耐张塔', '双回直线塔', '双回直线塔', '铁塔电缆支架']
# tower_type_high_list = ['J2-24', 'J4-24', 'FS-18', 'Z2-30', 'ZK-42', 'SJ2-24', 'SJ4-24', 'SZ2-30', 'SZK-42', '角钢']
# tower_weight_list = [6.8, 8.5, 7, 5.5, 8.5, 12.5, 17, 6.5, 10, 0.5, ]
# tower_height_list = [32, 32, 27, 37, 49, 37, 37, 42, 54, 0]
# tower_foot_distance_list = [5.5, 5.5, 6, 5, 6, 7, 8, 6, 8, 0]
#
# project02 = ElectricalInsulator(25.3, 23.6, 1.55, 3, 31, 5)
# project02.sum_cal_tower_type(tower_type_list, tower_type_high_list, tower_weight_list, tower_height_list, tower_foot_distance_list)
# project02.electrical_insulator_model(*insulator_list)
# print(project02.used_numbers_FXBW4_35_70, project02.used_numbers_U70BP_146D, project02.used_numbers_FPQ_35_4T16,
#       project02.used_numbers_YH5WZ_51_134)
