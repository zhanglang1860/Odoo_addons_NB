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
