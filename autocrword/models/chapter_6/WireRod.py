from ElectricalCircuit import ElectricalCircuit
from RoundUp import round_up


class WireRod(ElectricalCircuit):
    """
    线  材:
    钢芯铝绞线

    """

    def __init__(self, *value_list):
        # print(value_list)
        ElectricalCircuit.__init__(self, *value_list)
        self.aluminium_cable_steel_reinforced_type = ''
        self.aluminium_cable_steel_reinforced_length = 0
        self.aluminium_cable_steel_reinforced_weight = 0
        self.aluminium_cable_steel_reinforced_length_weight = 0

    def aluminium_cable_steel_reinforced(self, project_chapter6_type, aluminium_type):
        self.project_chapter6_type = project_chapter6_type
        self.aluminium_cable_steel_reinforced_type = aluminium_type
        if self.project_chapter6_type=='山区':
            if self.aluminium_cable_steel_reinforced_type == "LGJ_240_30":
                self.aluminium_cable_steel_reinforced_length = self.single_circuit * 3 * 1.05 + self.double_circuit * 6 * 1.05
                self.aluminium_cable_steel_reinforced_weight = 0.922
                self.aluminium_cable_steel_reinforced_length_weight = round_up(
                    self.aluminium_cable_steel_reinforced_length * self.aluminium_cable_steel_reinforced_weight, 2)
        elif self.project_chapter6_type=='平地':
            if self.aluminium_cable_steel_reinforced_type == "LGJ_240_30":
                self.aluminium_cable_steel_reinforced_length = self.single_circuit * 3 * 1.05 + self.double_circuit * 6 * 1.05
                self.aluminium_cable_steel_reinforced_weight = 0.922
                self.aluminium_cable_steel_reinforced_length_weight = round_up(
                    self.aluminium_cable_steel_reinforced_length * self.aluminium_cable_steel_reinforced_weight, 2)

        # return self.aluminium_cable_steel_reinforced_length_weight

#
# args_list = [25.3, 23.6, 1.55, 3, 31, 5]
# project02 = WireRod(*args_list)
# project02.aluminium_cable_steel_reinforced("LGJ-240/30")
# print(project02.aluminium_cable_steel_reinforced_length_weight)
