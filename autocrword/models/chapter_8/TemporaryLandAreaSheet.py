from RoundUp import round_dict
from docxtpl import DocxTemplate
import os
from ConstructionLandUseSummary import ConstructionLandUseSummary
from BoxVoltageDatabase import BoxVoltageDatabase
from BoosterStationDatabase import BoosterStationDatabase
from RoadBasementDatabase import RoadBasementDatabase


class TemporaryLandAreaSheet(ConstructionLandUseSummary):
    def __init__(self):
        self.wind_turbine_foundation, self.box_voltage_foundation, self.booster_station_foundation, \
        self.sum_foundation, self.sum_acres_foundation = 0, 0, 0, 0, 0

    def extraction_data_permanent_land_area(self):
        self.wind_turbine_foundation = self.total_2
        self.box_voltage_foundation = self.data_box_voltage.at[self.data_box_voltage.index[0], 'Area']
        self.booster_station_foundation = self.data_booster_station.at[self.data_booster_station.index[0], 'SlopeArea']
        self.sum_foundation = self.wind_turbine_foundation + self.box_voltage_foundation + self.booster_station_foundation
        self.sum_acres_foundation = self.sum_foundation / 666.667

    def generate_dict_permanent_land_area(self):
        dict_permanent_land_area = {
            '风电机组基础_永久用地面积': self.wind_turbine_foundation,
            '箱变基础_永久用地面积': self.box_voltage_foundation,
            '变电站_永久用地面积': self.booster_station_foundation,
            '合计_永久用地面积': self.sum_foundation,
            '合计亩_永久用地面积': self.sum_acres_foundation,
         }
        return dict_permanent_land_area
