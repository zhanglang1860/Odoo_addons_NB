from ElectricalCircuit import ElectricalCircuit


class WireRod(ElectricalCircuit):

    def __init__(self, *value_list):
        print(value_list)
        ElectricalCircuit.__init__(self, *value_list)
        self.aluminium_cable_steel_reinforced_type = ''
        self.aluminium_cable_steel_reinforced_length = 0
        self.aluminium_cable_steel_reinforced_weight = 0
        self.aluminium_cable_steel_reinforced_length_weight = 0

    def aluminium_cable_steel_reinforced(self, aluminium_type):
        self.aluminium_cable_steel_reinforced_type = aluminium_type
        if self.aluminium_cable_steel_reinforced_type == "LGJ-240/30":
            self.aluminium_cable_steel_reinforced_length = self.single_circuit * 3 * 1.05 + self.double_circuit * 6 * 1.05
            self.aluminium_cable_steel_reinforced_weight = 0.922
            self.aluminium_cable_steel_reinforced_length_weight = round(
                self.aluminium_cable_steel_reinforced_length * self.aluminium_cable_steel_reinforced_weight)
        # return self.aluminium_cable_steel_reinforced_length_weight


# project02 = WireRod(25.3, 23.6, 1.55, 3, 31, 5)
# project02.aluminium_cable_steel_reinforced("LGJ-240/30")
# print(project02.aluminium_cable_steel_reinforced_length_weight)
