from ElectricalCircuit import ElectricalCircuit


class Cable(ElectricalCircuit):
    """
    电缆
    """

    def __init__(self, *value_list):
        ElectricalCircuit.__init__(self, *value_list)

        self.cable_project = ''
        self.cable_project_list = []
        self.cable_model = ''
        self.cable_model_list = []
        self.cable_model_YJLV22_26_35_3_95_gaoya, self.cable_model_YJV22_26_35_1_300_gaoya = 0, 0
        self.cable_model_cable_duct = 0
        self.cable_model_YJLV22_26_35_3_95_dianlanzhongduan, self.cable_model_YJV22_26_35_1_300_dianlanzhongduan = 0, 0

    def cable_model(self, cable_project, cable_model):
        self.cable_project = cable_project
        self.cable_model = cable_model

        if self.project_chapter6_type == ["山地"]:
            if self.cable_project == "高压电缆":
                if self.cable_model == "YJLV22_26_35_3_95_gaoya":
                    self.cable_model_YJLV22_26_35_3_95_gaoya = self.buried_cable_35_3
                elif self.cable_model == "YJV22_26_35_1_300_gaoya":
                    self.cable_model_YJV22_26_35_1_300_gaoya = self.buried_cable_35_1
            if self.cable_project == "电缆沟":
                if self.cable_model == "电缆沟长度":
                    self.cable_model_cable_duct = 3.2
            if self.cable_project == "电缆终端":
                if self.cable_model == "YJLV22_26_35_3_95_dianlanzhongduan":
                    self.cable_model_YJLV22_26_35_3_95_dianlanzhongduan = self.tur_number * 2
                elif self.cable_model == "YJV22_26_35_1_300_dianlanzhongduan":
                    self.cable_model_YJV22_26_35_1_300_dianlanzhongduan = self.line_loop_number * 2

        if self.project_chapter6_type == ["平地"]:
            if self.cable_project == "高压电缆":
                if self.cable_model == "YJLV22_26_35_3_95_gaoya":
                    self.cable_model_YJLV22_26_35_3_95_gaoya = self.buried_cable_35_3
                elif self.cable_model == "YJV22_26_35_1_300_gaoya":
                    self.cable_model_YJV22_26_35_1_300_gaoya = self.buried_cable_35_1
            if self.cable_project == "电缆沟":
                if self.cable_model == "电缆沟长度":
                    self.cable_model_cable_duct = self.buried_cable_35_3+self.buried_cable_35_1
            if self.cable_project == "电缆终端":
                if self.cable_model == "YJLV22_26_35_3_95_dianlanzhongduan":
                    self.cable_model_YJLV22_26_35_3_95_dianlanzhongduan = self.tur_number * 2
                elif self.cable_model == "YJV22_26_35_1_300_dianlanzhongduan":
                    self.cable_model_YJV22_26_35_1_300_dianlanzhongduan = self.line_loop_number * 2

    def sum_cal_cable(self, cable_project_li, cable_li):
        self.cable_project_list = cable_project_li
        self.cable_model_list = cable_li

        for i in range(0, len(self.cable_project_list)):
            Cable.cable_model(self, self.cable_project_list[i], self.cable_model_list[i])

cable_project_list = ['高压电缆', '高压电缆', '电缆沟', '电缆终端', '电缆终端']
cable_model_list = ['YJLV22_26_35_3_95_gaoya', 'YJV22_26_35_1_300_gaoya', '电缆沟长度', 'YJLV22_26_35_3_95_dianlanzhongduan', 'YJV22_26_35_1_300_dianlanzhongduan']

project_chapter6_type = ['山地']
project02 = Cable(project_chapter6_type, 19, 22, 8, 1.5, 40, 6)

project02.sum_cal_cable(cable_project_list, cable_model_list)

print(project02.cable_model_YJLV22_26_35_3_95_gaoya, project02.cable_model_YJV22_26_35_1_300_gaoya,
      project02.cable_model_cable_duct,
      project02.cable_model_YJLV22_26_35_3_95_dianlanzhongduan, project02.cable_model_YJV22_26_35_1_300_dianlanzhongduan)

project_chapter6_type = ['平地']
project02 = Cable(project_chapter6_type, 25.3, 23.6, 1.55, 3, 31, 5)

project02.sum_cal_cable(cable_project_list, cable_model_list)

print(project02.cable_model_YJLV22_26_35_3_95_gaoya, project02.cable_model_YJV22_26_35_1_300_gaoya,
      project02.cable_model_cable_duct,
      project02.cable_model_YJLV22_26_35_3_95_dianlanzhongduan, project02.cable_model_YJV22_26_35_1_300_dianlanzhongduan)