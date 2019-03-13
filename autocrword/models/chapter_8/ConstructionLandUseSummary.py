import os
import pandas as pd
from RoundUp import round_dict
from docxtpl import DocxTemplate


class ConstructionLandUseSummary:
    def __init__(self):
        self.capacity, self.turbine_numbers = 0, 0
        self.material_warehouse_1, self.temporary_residential_office_1, self.steel_processing_plant_1, \
        self.equipment_storage_1, self.construction_machinery_parking_1, self.total_1 = 0, 0, 0, 0, 0, 0

        self.material_warehouse_2, self.temporary_residential_office_2, self.steel_processing_plant_2, \
        self.equipment_storage_2, self.construction_machinery_parking_2, self.total_2 = 0, 0, 0, 0, 0, 0

        self.data = pd.DataFrame()

    def extraction_data(self, capacity, turbine_numbers):
        self.capacity = capacity
        self.turbine_numbers = turbine_numbers

        if self.capacity * self.turbine_numbers <= 50:
            self.material_warehouse_1 = 200
            self.material_warehouse_2 = 1000
            self.temporary_residential_office_1 = 1800
            self.temporary_residential_office_2 = 3000
            self.steel_processing_plant_1 = 150
            self.steel_processing_plant_2 = 800
            self.equipment_storage_1 = 100
            self.equipment_storage_2 = 4500
            self.construction_machinery_parking_1 = 100
            self.construction_machinery_parking_2 = 1200

        elif self.capacity * self.turbine_numbers >= 100:
            self.material_warehouse_1 = 400
            self.material_warehouse_2 = 2000
            self.temporary_residential_office_1 = 2200
            self.temporary_residential_office_2 = 4000
            self.steel_processing_plant_1 = 250
            self.steel_processing_plant_2 = 1500
            self.equipment_storage_1 = 200
            self.equipment_storage_2 = 6500
            self.construction_machinery_parking_1 = 200
            self.construction_machinery_parking_2 = 1600
        else:
            self.material_warehouse_1 = 300
            self.material_warehouse_2 = 1500
            self.temporary_residential_office_1 = 2000
            self.temporary_residential_office_2 = 3500
            self.steel_processing_plant_1 = 200
            self.steel_processing_plant_2 = 1200
            self.equipment_storage_1 = 150
            self.equipment_storage_2 = 5500
            self.construction_machinery_parking_1 = 150
            self.construction_machinery_parking_2 = 1400
        self.total_1 = self.material_warehouse_1 + self.temporary_residential_office_1 + self.steel_processing_plant_1 + \
                       self.equipment_storage_1 + self.construction_machinery_parking_1
        self.total_2 = self.material_warehouse_2 + self.temporary_residential_office_2 + self.steel_processing_plant_2 + \
                       self.equipment_storage_2 + self.construction_machinery_parking_2

    def generate_dict(self):
        dict_construction_land_use_summary = {
            '材料仓库_1': self.material_warehouse_1,
            '材料仓库_2': self.material_warehouse_2,
            '临时住宅及办公室施工生活区_1': self.temporary_residential_office_1,
            '临时住宅及办公室施工生活区_2': self.temporary_residential_office_2,
            '钢筋加工厂_1': self.steel_processing_plant_1,
            '钢筋加工厂_2': self.steel_processing_plant_2,
            '设备存放场_1': self.equipment_storage_1,
            '设备存放场_2': self.equipment_storage_2,
            '施工机械停放场_1': self.construction_machinery_parking_1,
            '施工机械停放场_2': self.construction_machinery_parking_2,
            '合计_1': self.total_1,
            '合计_2': self.total_2,
        }
        return dict_construction_land_use_summary


project05 = ConstructionLandUseSummary()
project05.extraction_data(3, 15)
Dict = round_dict(project05.generate_dict())
print(Dict)
filename_box = ['cr8', 'result_chapter8']
save_path = r'C:\Users\Administrator\PycharmProjects\Odoo_addons_NB\autocrword\models\chapter_8'
read_path = os.path.join(save_path, '%s.docx') % filename_box[0]
save_path = os.path.join(save_path, '%s.docx') % filename_box[1]
tpl = DocxTemplate(read_path)
tpl.render(Dict)
tpl.save(save_path)
