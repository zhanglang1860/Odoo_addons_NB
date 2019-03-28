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
        self.electrical_insulator_type = ''
        self.electrical_insulator_name_li, self.electrical_insulator_type_li = [], []
        self.composite_insulator = ''
        self.porcelain_insulator = ''
        self.composite_pin_insulator = ''
        self.composite_zinc_oxide_protector = ''
        self.used_numbers_FXBW4_35_70 = 0
        self.used_numbers_U70BP_146D = 0
        self.used_numbers_FPQ_35_4T16 = 0
        self.used_numbers_YH5WZ_51_134 = 0

    def electrical_insulator_model(self, project_chapter6_ty, electrical_insulator_name_li,
                                   electrical_insulator_type_li):

        self.project_chapter6_type = project_chapter6_ty
        self.electrical_insulator_name_li = electrical_insulator_name_li
        self.electrical_insulator_type_li = electrical_insulator_type_li
        if self.project_chapter6_type == 1:
            for i in range(0, len(self.electrical_insulator_name_li)):
                self.electrical_insulator_name = self.electrical_insulator_name_li[i]
                self.electrical_insulator_type = self.electrical_insulator_type_li[i]
                if self.electrical_insulator_name == '复合绝缘子':
                    if self.electrical_insulator_type == 'FXBW4_35_70':
                        self.composite_insulator = 'FXBW4_35_70'
                elif self.electrical_insulator_name == '瓷绝缘子':
                    if self.electrical_insulator_type == 'U70BP_146D':
                        self.porcelain_insulator = 'U70BP_146D'
                elif self.electrical_insulator_name == '复合针式绝缘子':
                    if self.electrical_insulator_type == 'FPQ_35_4T16':
                        self.composite_pin_insulator = 'FPQ_35_4T16'
                elif self.electrical_insulator_name == '复合外套氧化锌避雷器':
                    if self.electrical_insulator_type == 'YH5WZ_51_134':
                        self.composite_zinc_oxide_protector = 'YH5WZ_51_134'

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
                                                            self.used_numbers_double_SJ2_24 + self.used_numbers_double_SJ4_24) * 12 +
                                                (
                                                            self.used_numbers_double_SZ2_30 + self.used_numbers_double_SZK_42) * 3) * 5

            if self.composite_pin_insulator == "FPQ_35_4T16":
                self.used_numbers_FPQ_35_4T16 = (self.tur_number + self.line_loop_number) * 12

            if self.composite_zinc_oxide_protector == "YH5WZ_51_134":
                self.used_numbers_YH5WZ_51_134 = (self.tur_number + self.line_loop_number) * 3


        if self.project_chapter6_type == 0:
            for i in range(0, len(self.electrical_insulator_name_li)):
                self.electrical_insulator_name = self.electrical_insulator_name_li[i]
                self.electrical_insulator_type = self.electrical_insulator_type_li[i]
                if self.electrical_insulator_name == '复合绝缘子':
                    if self.electrical_insulator_type == 'FXBW4_35_70':
                        self.composite_insulator = 'FXBW4_35_70'
                elif self.electrical_insulator_name == '瓷绝缘子':
                    if self.electrical_insulator_type == 'U70BP_146D':
                        self.porcelain_insulator = 'U70BP_146D'
                elif self.electrical_insulator_name == '复合针式绝缘子':
                    if self.electrical_insulator_type == 'FPQ_35_4T16':
                        self.composite_pin_insulator = 'FPQ_35_4T16'
                elif self.electrical_insulator_name == '复合外套氧化锌避雷器':
                    if self.electrical_insulator_type == 'YH5WZ_51_134':
                        self.composite_zinc_oxide_protector = 'YH5WZ_51_134'

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
                                                            self.used_numbers_double_SJ2_24 + self.used_numbers_double_SJ4_24) * 12 +
                                                (
                                                            self.used_numbers_double_SZ2_30 + self.used_numbers_double_SZK_42) * 3) * 5

            if self.composite_pin_insulator == "FPQ_35_4T16":
                self.used_numbers_FPQ_35_4T16 = (self.tur_number + self.line_loop_number) * 12

            if self.composite_zinc_oxide_protector == "YH5WZ_51_134":
                self.used_numbers_YH5WZ_51_134 = (self.tur_number + self.line_loop_number) * 3

# electrical_insulator_name_list = ['复合绝缘子', '瓷绝缘子', '复合针式绝缘子', '复合外套氧化锌避雷器']
# electrical_insulator_type_list = ['FXBW4_35_70', 'U70BP_146D', 'FPQ_35_4T16', 'YH5WZ_51_134']
#
# tower_type_list = ['单回耐张塔', '单回耐张塔', '单回耐张塔', '单回直线塔', '单回直线塔', '双回耐张塔', '双回耐张塔', '双回直线塔', '双回直线塔', '铁塔电缆支架']
# tower_type_high_list = ['J2_24', 'J4_24', 'FS_18', 'Z2_30', 'ZK_42', 'SJ2_24', 'SJ4_24', 'SZ2_30', 'SZK_42', '角钢']
# tower_weight_list = [6.8, 8.5, 7, 5.5, 8.5, 12.5, 17, 6.5, 10, 0.5, ]
# tower_height_list = [32, 32, 27, 37, 49, 37, 37, 42, 54, 0]
# tower_foot_distance_list = [5.5, 5.5, 6, 5, 6, 7, 8, 6, 8, 0]
#
# project_chapter6_type = ['山地']
# project02 = ElectricalInsulator(project_chapter6_type, 19, 22, 8, 1.5, 40, 6)
# project02.sum_cal_tower_type(tower_type_list, tower_type_high_list, tower_weight_list, tower_height_list,
#                              tower_foot_distance_list)
# project02.electrical_insulator_model(project_chapter6_type, electrical_insulator_name_list,
#                                      electrical_insulator_type_list)
# print(project02.used_numbers_FXBW4_35_70, project02.used_numbers_U70BP_146D, project02.used_numbers_FPQ_35_4T16,
#       project02.used_numbers_YH5WZ_51_134, project02.tur_number, project02.line_loop_number)
#
# project_chapter6_type = ['平地']
# project02 = ElectricalInsulator(project_chapter6_type, 25.3, 23.6, 1.55, 3, 31, 5)
# project02.sum_cal_tower_type(tower_type_list, tower_type_high_list, tower_weight_list, tower_height_list,
#                              tower_foot_distance_list)
#
# project02.electrical_insulator_model(project_chapter6_type, electrical_insulator_name_list,
#                                      electrical_insulator_type_list)
# print(project02.used_numbers_FXBW4_35_70, project02.used_numbers_U70BP_146D, project02.used_numbers_FPQ_35_4T16,
#       project02.used_numbers_YH5WZ_51_134, project02.tur_number, project02.line_loop_number)
