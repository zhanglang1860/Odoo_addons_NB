from ElectricalCircuit import ElectricalCircuit
from TowerType import TowerType


class ElectricalInsulator(ElectricalCircuit, TowerType):
    def __init__(self, *value_list):
        ElectricalCircuit.__init__(self, *value_list)
        self.composite_insulator = ''
        self.porcelain_insulator = ''
        self.composite_pin_insulator = ''
        self.composite_zinc_oxide_protector = ''
        self.used_numbers_FXBW4_35_70 = 0

    def electrical_insulator_model(self, composite_insulator, porcelain_insulator, composite_pin_insulator,
                                   composite_zinc_oxide_protector):
        self.composite_insulator = composite_insulator
        self.porcelain_insulator = porcelain_insulator
        self.composite_pin_insulator = composite_pin_insulator
        self.composite_zinc_oxide_protector = composite_zinc_oxide_protector

        if self.composite_insulator == "FXBW4-35/70":
            self.used_numbers_FXBW4_35_70 = \
                (self.used_numbers_single_Z2_30 + self.used_numbers_single_SZK_42) * 3 + (
                            self.used_numbers_double_SZ2_30 + self.used_numbers_double_SZK_42) * 3 + (
                            self.used_numbers_single_J2_24 + self.used_numbers_single_J4_24 + self.used_numbers_single_FS_18) * 4 + \
                (self.used_numbers_double_SJ2_24 + self.used_numbers_double_SJ4_24) * 6 + (
                            self.used_numbers_single_J2_24 + self.used_numbers_single_J4_24 + self.used_numbers_single_FS_18) * 12 + \
                (self.used_numbers_double_SJ2_24 + self.used_numbers_double_SJ4_24) * 12
