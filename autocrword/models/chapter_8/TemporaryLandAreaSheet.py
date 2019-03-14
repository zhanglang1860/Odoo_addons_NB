from RoundUp import round_dict
from docxtpl import DocxTemplate
import os, math
from ConstructionLandUseSummary import ConstructionLandUseSummary
from EarthStoneBalanceSheet import EarthStoneBalanceSheet
from PermanentLandAreaSheet import PermanentLandAreaSheet
from RoadBasementDatabase import RoadBasementDatabase


class TemporaryLandAreaSheet(ConstructionLandUseSummary, RoadBasementDatabase, PermanentLandAreaSheet,
                             EarthStoneBalanceSheet):
    def __init__(self):
        self.numbers_list_road, self.construction_auxiliary_enterprise, self.wind_turbine_installation_platform, \
        self.construction_road, self.waste_slag_yard, self.approach_road, self.overhead_line_land, \
        self.direct_buried_cable_land, self.sum_temporary_land_area = 0, 0, 0, 0, 0, 0, 0, 0, 0

    def extraction_data_temporary_land_area(self, numbers_list_road, overhead_line, direct_buried_cable):
        self.numbers_list_road = numbers_list_road

        self.construction_auxiliary_enterprise = self.total_2

        self.wind_turbine_installation_platform = \
            self.turbine_numbers * self.data_road_base_4.at[self.data_road_base_4.index[0], 'GeneralSiteLeveling_4'] - \
            self.wind_turbine_foundation - self.box_voltage_foundation

        self.construction_road = self.numbers_list_road[0] * 2.5 * 1000 + self.numbers_list_road[2] * \
                                 self.data_road_base_3.at[self.data_road_base_3.index[0], 'LandUse_3']

        self.waste_slag_yard = (math.floor(self.sum_EarthStoneBalance_spoil / 100000) + 1) * 10000

        self.approach_road = self.numbers_list_road[1] * self.data_road_base_3.at[
            self.data_road_base_3.index[0], 'LandUse_3']

        self.overhead_line_land = overhead_line
        self.direct_buried_cable_land = direct_buried_cable

        self.sum_temporary_land_area = self.construction_auxiliary_enterprise + self.wind_turbine_installation_platform + \
                                       self.construction_road + self.waste_slag_yard + self.approach_road + self.overhead_line_land + \
                                       self.direct_buried_cable_land


def generate_dict_permanent_land_area(self):
    dict_permanent_land_area = {
        '风电机组基础_永久用地面积': self.wind_turbine_foundation,
        '箱变基础_永久用地面积': self.box_voltage_foundation,
        '变电站_永久用地面积': self.booster_station_foundation,
        '合计_永久用地面积': self.sum_foundation,
        '合计亩_永久用地面积': self.sum_acres_foundation,
    }
    return dict_permanent_land_area
