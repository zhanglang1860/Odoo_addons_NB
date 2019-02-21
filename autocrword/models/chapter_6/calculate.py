# import decimal
# from decimal import *
#
# Context(prec=4, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999, capitals=1, clamp=0, flags=[],
#         traps=[InvalidOperation, DivisionByZero, Overflow])


class ElectricalCircuit:
    def __init__(self, single_circuit, double_circuit, buried_cable_35_1, buried_cable_35_3, tur_number,
                 line_loop_number):
        self.single_circuit = single_circuit
        self.double_circuit = double_circuit
        self.buried_cable_35_1 = buried_cable_35_1
        self.buried_cable_35_3 = buried_cable_35_3
        self.tur_number = tur_number
        self.line_loop_number = line_loop_number

        self.aluminium_cable_steel_reinforced_type = ''
        self.aluminium_cable_steel_reinforced_length = 0
        self.aluminium_cable_steel_reinforced_weight = 0
        self.aluminium_cable_steel_reinforced_weight_length = 0


class WireRod(ElectricalCircuit):
    def aluminium_cable_steel_reinforced(self, aluminium_type):
        self.aluminium_cable_steel_reinforced_type = aluminium_type
        if self.aluminium_cable_steel_reinforced_type == "LGJ-240/30":
            self.aluminium_cable_steel_reinforced_length = self.single_circuit * 3 * 1.05 + self.double_circuit * 6 * 1.05
            self.aluminium_cable_steel_reinforced_weight = 0.922
            self.aluminium_cable_steel_reinforced_weight_length = round(
                self.aluminium_cable_steel_reinforced_length * self.aluminium_cable_steel_reinforced_weight)
        return self.aluminium_cable_steel_reinforced_weight_length


class TowerType(ElectricalCircuit):
    def __init__(self, *value_list):
        ElectricalCircuit.__init__(self, *value_list)
        self.tower_type = ''
        self.tower_type_high = ''
        self.used_numbers = ''
        self.tower_weight = 0
        self.tower_number_weight = 0
        self.tower_height = 0
        self.tower_foot_distance = 0

        self.tower_area = 0
        self.sum_tower_area = 0
        self.tower_number_area = []
        self.sum_used_numbers = 0
        self.sum_tower_number_weight = 0
        self.kilometer_tower_number = 0

    def tower_type_models(self, tower_type, tower_type_high, tower_weight, tower_height, tower_foot_distance):
        self.tower_type = tower_type
        self.tower_type_high = tower_type_high
        self.tower_weight = tower_weight
        self.tower_height = tower_height
        self.tower_foot_distance = tower_foot_distance

        if self.tower_type == "单回耐张塔":
            if self.tower_type_high == "J2-24" or self.tower_type_high == "J4-24":
                self.used_numbers = round(self.single_circuit / 3, 0)
                self.tower_number_weight = self.tower_weight * self.used_numbers
                self.tower_area = self.used_numbers * self.tower_foot_distance ** 2
            elif self.tower_type_high == "FS-18":
                self.used_numbers = round(((self.line_loop_number * 100 / 2) / 100 + 1), 0)
                self.tower_number_weight = self.tower_weight * self.used_numbers
                self.tower_area = self.used_numbers * self.tower_foot_distance ** 2

        if self.tower_type == "单回直线塔":
            if self.tower_type_high == "Z2-30" or self.tower_type_high == "ZK-42":
                self.used_numbers = round(self.single_circuit * 1000 / 250 / 2, 0)
                self.tower_number_weight = self.tower_weight * self.used_numbers
                self.tower_area = self.used_numbers * self.tower_foot_distance ** 2

        if self.tower_type == "双回耐张塔":
            if self.tower_type_high == "SJ2-24" or self.tower_type_high == "SJ4-24":
                self.used_numbers = round(self.double_circuit / 3, 0)
                self.tower_number_weight = self.tower_weight * self.used_numbers
                self.tower_area = self.used_numbers * self.tower_foot_distance ** 2

        if self.tower_type == "双回直线塔":
            if self.tower_type_high == "SZ2-30" or self.tower_type_high == "SZK-42":
                self.used_numbers = round(self.double_circuit * 1000 / 220 / 2, 0)
                self.tower_number_weight = self.tower_weight * self.used_numbers
                self.tower_area = self.used_numbers * self.tower_foot_distance ** 2

        if self.tower_type == "铁塔电缆支架":
            if self.tower_type_high == "角钢":
                self.used_numbers = self.tur_number
                self.tower_number_weight = self.tower_weight * self.used_numbers
                self.tower_area = 0

    def sum_cal(self, tower_type_list, tower_type_high_list, tower_weight_list, tower_height_list,
                tower_foot_distance_list):
        for i in range(0, len(tower_weight_list)):
            TowerType.tower_type_models(self, tower_type_list[i], tower_type_high_list[i], tower_weight_list[i],
                                        tower_height_list[i], tower_foot_distance_list[i])
            print(self.tower_type, self.tower_type_high, self.used_numbers)
            if self.tower_type == "铁塔电缆支架":
                self.sum_used_numbers = self.sum_used_numbers
            else:
                self.sum_used_numbers = int(self.used_numbers) + self.sum_used_numbers
            self.sum_tower_number_weight = float(self.tower_number_weight) + self.sum_tower_number_weight
            self.tower_number_area.append(self.tower_area)
            self.kilometer_tower_number = self.sum_used_numbers / (self.single_circuit + self.double_circuit)
            self.sum_tower_area = float(self.tower_area) + self.sum_tower_area


# project01 = ElectricalCircuit(25.3, 23.6, 1.55, 3, 31, 5)
project02 = TowerType(25.3, 23.6, 1.55, 3, 31, 5)
tower_type_list = ['单回耐张塔', '单回耐张塔', '单回耐张塔', '单回直线塔', '单回直线塔', '双回耐张塔', '双回耐张塔', '双回直线塔', '双回直线塔', '铁塔电缆支架']
tower_type_high_list = ['J2-24', 'J4-24', 'FS-18', 'Z2-30', 'ZK-42', 'SJ2-24', 'SJ4-24', 'SZ2-30', 'SZK-42', '角钢']
tower_weight_list = [6.8, 8.5, 7, 5.5, 8.5, 12.5, 17, 6.5, 10, 0.5, ]
tower_height_list = [32, 32, 27, 37, 49, 37, 37, 42, 54, 0]
tower_foot_distance_list = [5.5, 5.5, 6, 5, 6, 7, 8, 6, 8, 0]
project02.sum_cal(tower_type_list, tower_type_high_list, tower_weight_list, tower_height_list, tower_foot_distance_list)

print(project02.sum_tower_area)
